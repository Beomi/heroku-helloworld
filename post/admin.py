from django.contrib import admin

from .models import Post, Image, Comment, Category


@admin.register(Post, Image, Comment, Category)
class DefaultAdmin(admin.ModelAdmin):
    pass