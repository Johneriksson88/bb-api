from django.contrib import admin
from .models import Mood

# register mood to admin panel
admin.site.register(Mood)
