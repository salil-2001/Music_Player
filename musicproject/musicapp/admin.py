from django.contrib import admin
from .models import Artist,Album,Song

admin.site.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display=('id','name','created','last_update')

admin.site.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display=('id','artist','album_name','created','last_update')

admin.site.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=('id','album','song_thumbnail','song','song_name','created','last_update')

    