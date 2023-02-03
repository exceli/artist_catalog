from django.db import models


class Artist(models.Model):
    """ Artist model """
    pseudonym = models.CharField(max_length=255, verbose_name='Pseudonym')


    def __str__(self):
        return self.pseudonym


class Album(models.Model):
    """ Album model """
    title = models.CharField(max_length=255, verbose_name='Title')
    artist = models.ForeignKey('Artist', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Artist')
    year_of_issue = models.DateField(verbose_name='Year of issue')

    def __str__(self):
        return self.title


class Song(models.Model):
    """ Song model """
    name = models.CharField(max_length=255, verbose_name='Name')
    album_number = models.PositiveIntegerField(blank=True, null=True, verbose_name='Song number in album')
    artist = models.ForeignKey('Artist', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Artist')
    album = models.ForeignKey('Album', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Album')

    def __str__(self):
        return self.name

