# accounts/admin.py
from django.contrib import admin
from .models import MagicLink

admin.site.register(MagicLink)