from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'phone_number', 'email', 'birthdate')
    list_display_links = ('id', 'username', 'first_name', 'last_name', )
    search_fields = ('id', 'username', 'first_name', 'last_name', 'phone_number', 'email', 'birthdate', 'is_published')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address')
    list_display_links = ('id', 'user', )


admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(CustomUser, UserAdmin)