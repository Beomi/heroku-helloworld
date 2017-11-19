from django.db import models


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(TimeStampedModel):
    category = models.ForeignKey('Category')
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    post = models.ForeignKey('Post')
    content = models.TextField()

    def __str__(self):
        return self.post.title + ': ' + self.content


class Category(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
