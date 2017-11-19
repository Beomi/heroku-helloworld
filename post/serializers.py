from rest_framework import serializers

from .models import Post, Comment, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
