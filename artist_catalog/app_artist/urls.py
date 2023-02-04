from django.urls import path

from .views import SongAPIList, ArtistAPIList, AlbumAPIList


urlpatterns = [
    path('songs/', SongAPIList.as_view(), name='songs'),
    path('artists/', ArtistAPIList.as_view(), name='artists'),
    path('albums/', AlbumAPIList.as_view(), name='albums'),
]