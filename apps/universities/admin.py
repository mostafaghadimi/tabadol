from django.contrib import admin
from .models import University

class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'longitude', 'lattitude']
    

admin.site.register(University, UniversityAdmin)
