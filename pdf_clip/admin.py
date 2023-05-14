from django.contrib import admin
from .models import Clip, File, Position

# Register your models here.
admin.site.register(Clip)
admin.site.register(File)
admin.site.register(Position)