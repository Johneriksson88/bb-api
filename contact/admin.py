from django.contrib import admin
from .models import Contact

# register contact to admin panel
admin.site.register(Contact)