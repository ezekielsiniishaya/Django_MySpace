from django.contrib import admin
from .models import CustomUser, UserNotes

admin.site.register(UserNotes)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'name', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)