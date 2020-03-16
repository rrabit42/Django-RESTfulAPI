from django.contrib.auth.models import User
from rest_framework import status, mixins, generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # REST 프레임워크는 특정 뷰에 제한을 걸 수 있는 권한 클래스를 제공하고 있음. 그 중 한가지인 IsAUthenticatedOrReadOnly는 인증 받은 요청에 읽기, 쓰기 권한 부여, 인증 받지 않은 요청은 읽기 권한만 부여

    def perform_create(self, serializer): # 이 메서드는 인스턴스를 저장하는 과정을 조정, 라서 요청이나 요청 URL에서 정보를 가져와 원하는 대로 다룰 수 있음.
        serializer.save(owner=self.request.user) # 우리가 만든 시리얼라이저의 create() 메서드는 검증한 요청 데이터에 더하여 'owner' 필드도 전달.


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(('GET', ))
def api_root(request, format=None):
    return Response({
        # url 만드는데 reverse 함수 사용
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetHighlight(generics.GenericAPIView):
    # Rest 프레임워크에서 HTML로 렌더링하는 방식은 두가지가 있음
    # 1. 템플릿 사용
    # 2. 미리 렌더링된 HTML 사용(우리가 할 것)
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)