from django.contrib import admin
from project.models import Image


# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display=("image","title","writer")
admin.site.register(Image,ImageAdmin)