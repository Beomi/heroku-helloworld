from django.conf.urls import url, include
from rest_framework import routers

from .views import PostViewSet, CommentViewSet, CategoryViewSet

router = routers.DefaultRouter()
# Register routers
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
