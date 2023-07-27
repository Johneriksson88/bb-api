from django.db import models
from django.contrib.auth.models import User

'''
Mood model is related to Post model through many-to-many field in the Post model.
Many-to-many field creates an intermittent table that connects mood id to post id and has its own id.
'''
class Mood(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.id} {self.name}'