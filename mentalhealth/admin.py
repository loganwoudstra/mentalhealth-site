from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Entry, CheckIn
# Register your models here.
admin.site.register(Entry)
admin.site.register(CheckIn)