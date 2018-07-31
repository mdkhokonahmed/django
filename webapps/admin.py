from django.contrib import admin
from .models import Category,Post,Slider,Logo
# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Slider)
admin.site.register(Logo)