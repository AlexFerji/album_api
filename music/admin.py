from django.contrib import admin
from .models import Album, Track, Artist

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']



class TrackAdmin(admin.ModelAdmin):
    list_display = ['album', 'order', 'title']



class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_name', 'artist']


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Album, AlbumAdmin)
