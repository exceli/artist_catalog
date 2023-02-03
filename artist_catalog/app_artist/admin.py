from django.contrib import admin

from app_artist.models import Song, Artist, Album

admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Album)
