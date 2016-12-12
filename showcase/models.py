from __future__ import unicode_literals
import operator

from django.db import models
from django.db.models import Q

# TODO: Add tags in storyboard object, consider using a package
# TODO: Consider outsourcing the preview image from the beatmap thumbnails as a choice.
# TODO: That manager is not working. I'll need to learn about search filters way better.

class StoryboardManager(models.Manager):
    def search(self, search_terms):
        terms = [term.strip() for term in search_terms.split()]
        q_objects = []

        for term in terms:
            q_objects.append(Q(song__icontains=term))
            q_objects.append(Q(artist__icontains=term))
            q_objects.append(Q(storyboarder__icontains=term))

        qs = self.get_queryset()

        return qs.filter(reduce(operator.or_, q_objects))

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
    objects = StoryboardManager()

    def __str__(self):
        return "%s - %s" % (self.artist, self.song)

class Storyboarder(models.Model):
    username = models.CharField(max_length=64)
    avatar = models.ImageField(blank=True)
    profile = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.username
