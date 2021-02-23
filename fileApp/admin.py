from django.contrib import admin
from .models import Image, Category, Product, Choice

# Register your models here.
admin.site.register(Image)

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(Choice)