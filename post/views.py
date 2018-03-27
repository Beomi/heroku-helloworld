from rest_framework import viewsets

from .models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() \
        .prefetch_related('comment_set')
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
