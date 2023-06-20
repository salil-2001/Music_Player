from django.db import models
from django.utils.translation import gettext_lazy as _ 


class Artist(models.Model):
    name=models.CharField(_("Artist Name"),max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name=("Artist")
        verbose_name_plural=("Artists")

    def __str__(self):
        return self.name
    
class Album(models.Model):
    artist=models.ForeignKey(Artist,verbose_name=("Artist Album"),on_delete=models.CASCADE)
    album_name=models.CharField(_("Album Name"),max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name=("Album")
        verbose_name_plural=("Albums")

    def __str__(self):
        return self.album_name


class Song(models.Model):
    album=models.ForeignKey(Album,verbose_name=("Song Album"),on_delete=models.CASCADE)
    song_thumbnail=models.ImageField(_("Song Thumbnail"), upload_to='thumbnail/',help_text=".jpg,.png,.jepg,.gif,.svg Supported")
    song=models.FileField(_("Song"),upload_to="songs/",help_text=".mp3 Support only")
    song_name=models.CharField(_("Song Name"),max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name=("Song")
        verbose_name_plural=("Songs")


    def __str__(self):
        return self.song_name
