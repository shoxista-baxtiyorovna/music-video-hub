from django.db import models
from django.shortcuts import reverse


class Track(models.Model):
    music_title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.TextField(max_length=300)
    genre = models.TextField(max_length=500)
    release_date = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='image/')
    audio_file = models.FileField(upload_to='audio/')

    def get_detail_url(self):
        return reverse('tracks:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('tracks:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('tracks:update', args=[self.pk])

