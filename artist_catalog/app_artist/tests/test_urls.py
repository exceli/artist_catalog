from django.urls import reverse

from app_artist.tests.test_settings import SettingsSongArtistAlbum


class SongUrlsTest(SettingsSongArtistAlbum):
    def test_song_url_login(self):
        self.client.login(username='test@gmail.test', password='test123test')
        url = reverse('songs')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_song_url_not_login_user(self):
        url = reverse('songs')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


