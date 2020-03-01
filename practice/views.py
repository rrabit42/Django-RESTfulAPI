from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions


# 실질적으로 Queryset을 컨트롤하고 데이터를 조작해
# Serializer을 통해 매핑을 시켜주는 View를 작성
# 여러개의 뷰를 작성하지 않고, Viewset을 이용해 Model 하나를 컨트롤하는 CRUD를
# 1개의 CBView 로 구현시킴
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
