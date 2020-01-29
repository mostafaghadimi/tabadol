
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

from .models import Profile

# The following changes are to aggregate Profile and User models!
class ProfileInline(admin.StackedInline):
    verbose_name_plural = 'Profile'
    can_delete = False
    model = Profile
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    
    list_display = ('username', 'email', 'get_university', 'get_discipline')

    def get_university(self, instance):
        return instance.profile.university

    def get_discipline(self, instance):
        return instance.profile.discipline

    #Attributes name shown in admin    
    get_university.short_description = 'University'
    get_discipline.short_description = 'discipline'


    def get_inline_instances(self, request, obj = None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
        

