from django.urls import path
from snippets import views
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

# View 클래스 대신 ViewSet 클래스를 사용했기 때문에, 이제는 URL도 설정할 필요가 없습니다.
# Router 클래스를 사용하면 뷰 코드와 뷰, URL이 관례적으로 자동 연결됩니다.
# 단지 뷰를 라우터에 적절히 등록해주기만 하면 됩니다. 그러면 REST 프레임워크가 알아서 다 합니다.

#라우터를 생성하고 뷰셋을 등록합니다
router = DefaultRouter() # DefaultRouter 클래스는 API의 최상단 뷰를 자동으로 생성해주므로, views 모듈에 있는 api_root 메서드와 연결했던 URL도 삭제하였습니다.
router.register('snippets', views.SnippetViewSet) # 뷰들에 사용할 url 접두어와 뷰셋 등록
router.register('users', views.User)

# 이제 API URL을 라우터가 자동으로 인식합니다
# 추가로 탐색 가능한 API를 구현하기 위해 로그인에 사용할 URL은 직접 설정을 했습니다.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]