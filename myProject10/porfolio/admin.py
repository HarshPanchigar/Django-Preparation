from django.contrib import admin

# Register your models here.
from porfolio.models import Student , Profile


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name' , 'age' , 'city')
    search_fields = ('id','name' , 'age' , 'city')
    list_filter = ('age','city')
    ordering = ('name',)

admin.site.register(Profile)
