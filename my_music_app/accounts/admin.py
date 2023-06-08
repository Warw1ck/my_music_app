from django.contrib import admin

# Register your models here.
from my_music_app.accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass