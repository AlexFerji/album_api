from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return  self.name


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist_name')
    date = models.DateField()


    def __str__(self):
        return  self.album_name


class Track(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist_track')
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField(unique=False)
    title = models.CharField(max_length=100)

    def __str__(self):
        return '{0} {1}'.format(self.order, self.title)





