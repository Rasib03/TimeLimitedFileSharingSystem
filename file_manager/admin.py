from django.contrib import admin
from .models import SharedFile

@admin.register(SharedFile)
class SharedFileAdmin(admin.ModelAdmin):
    # Admin panel mein kaun kaun se columns dikhne chahiye
    list_display = ('title', 'master_user', 'upload_time', 'duration_hrs', 'is_editable')
    # Master user ko manually select karne ke liye
    fields = ('master_user', 'title', 'file', 'duration_hrs', 'allowed_users')