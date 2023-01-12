from django.contrib import admin

from .models import Category, Image, Blog, Tag

admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Blog)
admin.site.register(Tag)
