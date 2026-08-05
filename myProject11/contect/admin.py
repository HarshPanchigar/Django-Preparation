from django.contrib import admin
from .models import Contect

@admin.register(Contect)
class ContectRegister(admin.ModelAdmin):
    list_display = ('name' , 'message' , 'created_at')
    