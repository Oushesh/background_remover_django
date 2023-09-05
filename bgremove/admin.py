from django.contrib import admin

# Register your models here.
from .models import UserActivity

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ["slug", "image", "result", "created_at"]
