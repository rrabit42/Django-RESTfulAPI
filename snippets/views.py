from django.contrib.auth.models import User
from rest_framework import status, mixins, generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer): # 이 메서드는 인스턴스를 저장하는 과정을 조정, 라서 요청이나 요청 URL에서 정보를 가져와 원하는 대로 다룰 수 있음.
        serializer.save(owner=self.request.user) # 우리가 만든 시리얼라이저의 create() 메서드는 검증한 요청 데이터에 더하여 'owner' 필드도 전달.


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
