from django.core.exceptions import ValidationError

from app_artist.models import Artist, Album, Song
from app_artist.tests.test_settings import SettingsSongArtistAlbum


class ArtistModelTest(SettingsSongArtistAlbum):
    def test_validators_value(self):
        self.assertTrue(self.artist)
        self.assertEqual(self.artist._meta.get_field('pseudonym').max_length, 255)

    def test_validation_fail(self):
        artist_invalid_pseudonym = Artist(pseudonym='')
        with self.assertRaises(ValidationError):
            artist_invalid_pseudonym.full_clean()
            artist_invalid_pseudonym.save()


class AlbumModelTest(SettingsSongArtistAlbum):
    def test_validators_value(self):
        self.assertTrue(self.album)
        self.assertEqual(self.album._meta.get_field('title').max_length, 255)

    def test_validation_fail(self):
        album_invalid_title = Album(title='', artist=self.artist, year_of_issue='2021')
        with self.assertRaises(ValidationError):
            album_invalid_title.full_clean()
            album_invalid_title.save()


class SongModelTest(SettingsSongArtistAlbum):
    def test_validators_value(self):
        self.assertTrue(self.song1)
        self.assertEqual(self.song1._meta.get_field('name').max_length, 255)


    def test_validation_fail(self):
        song_invalid_album_number = Song(name='Test song1', album_number=1, album=self.album)
        with self.assertRaises(ValidationError):
            song_invalid_album_number.full_clean()
            song_invalid_album_number.save()



