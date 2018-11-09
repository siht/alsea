from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    status = models.CharField(max_length=64)
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'artist_group'


class Album(models.Model):
    title = models.CharField(max_length=128, db_index=True)
    number_tracks = models.IntegerField()
    publish_date = models.DateField()
    artist = models.ForeignKey('Artist', on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'album'
