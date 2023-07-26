from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=False)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.owner} - {self.title}"
