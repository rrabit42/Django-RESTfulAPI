from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tutorial import views


# Because we're using viewsets instead of views, we can automatically generate the URL conf for our API, by simply registering the viewsets with a router class.
# Again, if we need more control over the API URLs we can simply drop down to using regular class-based views, and writing the URL conf explicitly.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)    # http://127.0.0.1:8000/users/ 가능, 밑에 include(router.urls)때문
router.register(r'groups', views.GroupViewSet)  # http://127.0.0.1:8000/groups/ 가능, 밑에 include(router.urls)때문

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('practice.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]