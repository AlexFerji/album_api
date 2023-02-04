from rest_framework import serializers
from .models import Album, Artist, Track


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(many=False,
                                          queryset=Artist.objects.all(),
                                          slug_field='name')

    class Meta:
        model = Album
        fields = ['album_name', 'artist',  'date']
        extra_kwargs = {
            'tracks': {'write_only': True},
        }


class ArtistSerializers(serializers.ModelSerializer):
    name = serializers.CharField()
    tracks = serializers.StringRelatedField(source='artist_track',
                                            many=True)

    class Meta:
        model = Artist
        fields = ('__all__')


class TrackSerializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(many=False,
                                          queryset=Artist.objects.all(),
                                          slug_field='name')
    album = serializers.SlugRelatedField(many=False,
                                         queryset=Album.objects.all(),
                                         slug_field='album_name')

    class Meta:
        model = Track
        fields = ('__all__')


