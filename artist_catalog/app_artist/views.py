from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Song, Artist, Album
from .serializers import SongSerializer, ArtistSerializer, AlbumSerializer


class APIListPagination(PageNumberPagination):
    """ Pagination for views """
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5


class SongAPIList(ListCreateAPIView):
    """ View to get list of songs """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = APIListPagination


class ArtistAPIList(ListCreateAPIView):
    """ View to get list of artists """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAuthenticated, )


class AlbumAPIList(ListCreateAPIView):
    """ View to get list of albums """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAuthenticated, )

