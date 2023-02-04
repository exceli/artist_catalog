from rest_framework.serializers import ModelSerializer

from .models import Song, Artist, Album


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ('name', 'album_number', 'album',)


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ('pseudonym',)


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ('title', 'artist', 'year_of_issue',)
