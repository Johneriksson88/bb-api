from django.db import models
from django.contrib.auth.models import User
from moods.models import Mood

# post model
class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    song = models.CharField(max_length=255)
    link = models.CharField(max_length=255, default="")
    content = models.TextField(blank=True)
    moods = models.ManyToManyField(Mood, related_name="posts", blank=False)
    image = models.ImageField(
        upload_to='images/', default='../default_post_vzfmrq', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'