from __future__ import unicode_literals
import operator

from django.db import models
from django.db.models import Q

# TODO: Add tags in storyboard object, consider using a package
# TODO: Consider outsourcing the preview image from the beatmap thumbnails as a choice.

class Storyboard(models.Model):
    # Sortables
    song = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    storyboarder =  models.ForeignKey('Storyboarder', on_delete=models.CASCADE)
    mapper = models.CharField(max_length=64)
    date_added = models.DateTimeField()
    date_created = models.DateTimeField()
    medium = models.CharField(max_length=64)
    featured = models.BooleanField()
    classic = models.BooleanField()
    # Non-sortables
    preview = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    video = models.URLField(blank=True)
    download = models.URLField(blank=True)

    def __str__(self):
        return "%s - %s" % (self.artist, self.song)

class Storyboarder(models.Model):
    username = models.CharField(max_length=64)
    avatar = models.ImageField(blank=True)
    profile = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.username