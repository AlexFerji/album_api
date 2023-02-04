from rest_framework import viewsets
from .serializers import AlbumSerializer, ArtistSerializers, TrackSerializer
from .models import Album, Artist, Track


class ArtistListCreate(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers
    http_method_names = ['post', 'get', ' put']


class TrackListCreate(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    http_method_names = ['post', 'get', 'put', 'delete']


class AlbumListCreate(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    http_method_names = ['post', 'get', 'put', 'delete']






