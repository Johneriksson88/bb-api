from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Mood(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)
    emoji = models.CharField(max_length=10)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.id} {self.name}'