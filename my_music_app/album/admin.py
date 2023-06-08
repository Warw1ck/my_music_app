from django.contrib import admin

# Register your models here.
from my_music_app.album.models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass