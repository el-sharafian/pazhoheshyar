from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('personal_id', 'username', 'email', 'degree', 'student_id', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('personal_id', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'username', 'email', 'degree', 'student_id')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('personal_id', 'password1', 'password2'),
        }),
        ('Personal info', {'fields': ('first_name', 'last_name', 'username', 'email', 'degree', 'student_id')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    search_fields = ('personal_id', 'username', 'email', 'degree', 'student_id')
    ordering = ('personal_id',)
