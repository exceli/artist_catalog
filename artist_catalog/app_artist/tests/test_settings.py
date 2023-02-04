from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient

from app_artist.models import Artist, Album, Song


class SettingsSongArtistAlbum(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.client = APIClient()
        cls.user = get_user_model().objects.create_user(
            'test@gmail.test',
            'test123test'
        )
        cls.client.force_authenticate(cls.user)

        cls.artist = Artist.objects.create(
            pseudonym='Test pseudonym',
        )
        cls.artist.save()

        cls.album = Album.objects.create(
            title='Test album1',
            artist=cls.artist,
            year_of_issue='2002-03-04',
        )
        cls.album.save()

        cls.song1 = Song.objects.create(
            name='Test song1',
            album_number=1,
            album=cls.album,
        )
        cls.song1.save()

        cls.song2 = Song.objects.create(
            name='Test song2',
            album_number=2,
            album=cls.album,
        )
        cls.song2.save()


    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
