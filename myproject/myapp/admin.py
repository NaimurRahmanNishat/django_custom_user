from django.contrib import admin
from .models import *
# Register your models here.
class Display_List(admin.ModelAdmin):
    list_display=['username', 'UserType', 'Education']

admin.site.register(CustomUserModel, Display_List)