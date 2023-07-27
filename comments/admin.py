from django.contrib import admin
from .models import Comment

# register comment to admin panel
admin.site.register(Comment)
