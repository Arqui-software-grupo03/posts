from django.conf.urls import url, include
from django.urls import path, re_path
from django.contrib import admin

from rest_framework import routers, schemas
from posts import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'hashtags', views.HashtagViewSet)
router.register(r'posts/(?P<post>[^/.]+)/answers', views.AnswerViewSet)

schema_view = schemas.get_schema_view(title="Posts API")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    path('schema/', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    # re_path('api/(?P<version>(v1|v2))/', include('posts.urls'))
]
