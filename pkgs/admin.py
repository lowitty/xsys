from django.contrib import admin

# Register your models here.
from .models import User, Node

admin.site.register(User)
admin.site.register(Node)