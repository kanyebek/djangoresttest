from django.urls import path
from .views import PostViewSet, CommentViewSet

urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:id>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('posts/<int:post_id>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
]