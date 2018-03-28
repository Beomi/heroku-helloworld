from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Image(TimeStampedModel):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.image.file.name


class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.post.title + ': ' + self.content


class Category(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
