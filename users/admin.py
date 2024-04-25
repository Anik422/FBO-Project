# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser



admin.site.site_header = "FBO Membership Admin"
admin.site.site_title = "FBO Membership Admin Area"
admin.site.index_title = "Welcome to the FBO Membership admin area"



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'username', 'password1', 'password2'),
        }),
    )
    # Add any other customizations as needed

admin.site.register(CustomUser, CustomUserAdmin)
