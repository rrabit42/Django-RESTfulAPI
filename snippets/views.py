from django.contrib.auth.models import User
from rest_framework import status, mixins, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


class SnippetViewSet(viewsets.ModelViewSet): # 읽기 기능과 쓰기 기능을 모두 지원하기 위해 ModelViewSet 사용
    """
    이 뷰셋은 `list`와 `create`, `retrieve`, `update`, `destroy` 기능을 자동으로 지원합니다.

        여기에 `highlight` 기능의 코드만 추가로 작성했습니다.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # This decorator can be used to add any custom endpoints that don't fit into the standard create/update/delete style.
    # Custom actions which use the @action decorator will respond to GET requests by default. We can use the methods argument if we wanted an action that responded to POST requests.
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet): # ReadOnlyModelViewSet은 '읽기 전용' 기능을 자동 지원
    """
    이 뷰셋은 `list`와 `detail` 기능을 자동으로 지원합니다
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(('GET', ))
def api_root(request, format=None):
    return Response({
        # url 만드는데 reverse 함수 사용
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


