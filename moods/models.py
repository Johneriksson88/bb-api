""" from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    post = models.ManyToOneRel(field, to, field_name)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.name}' """