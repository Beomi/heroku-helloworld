from rest_framework import serializers

from .models import Post, Comment, Category


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Post
        fields = (
            'id', 'user', 'category', 'title', 'content', 'comment_set',
        )
