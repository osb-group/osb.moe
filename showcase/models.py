from __future__ import unicode_literals
import operator

from django.db import models
from django.db.models import Q
from photologue.models import Gallery


class Storyboard(models.Model):
    # Constants
    MEDIUMS = (
        ('design', 'Design Editor'),
        ('osb', 'Scripting'),
        ('sgl', 'osu!SGL'),
        ('c', 'C'),
        ('cplusplus','C++'),
        ('csharp','C#'),
        ('java','Java'),
        ('python','Python'),
        ('storybrew','Storybrew'),
        ('other','Other')
    )
    # Sortables
    song = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    set_id = models.BigIntegerField(blank=True)
    storyboarder = models.ManyToManyField('Storyboarder')
    mapper = models.CharField(max_length=64)
    date_added = models.DateTimeField()
    date_created = models.DateTimeField()
    medium = models.CharField(max_length=64,choices=MEDIUMS,default='other')
    featured = models.BooleanField()
    classic = models.BooleanField()
    # Non-sortables
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True)
    comments = models.TextField(blank=True)
    description = models.TextField(blank=True)
    video = models.URLField(blank=True)

    def __str__(self):
        return "%s - %s" % (self.artist, self.song)

class Storyboarder(models.Model):
    # Constants
    ROLES = (
        ('owner', 'Server Owner'),
        ('mentor', 'Mentor'),
        ('storyboarder', 'Storyboarder'),
        ('apprentice', 'Apprentice'),
        ('other', 'Other'),
    )
    username = models.CharField(max_length=64)
    avatar = models.ImageField(blank=True, upload_to='a')
    profile = models.URLField(blank=True)
    title = models.CharField(max_length=64,blank=True,default='Storyboarder')
    role = models.CharField(max_length=64,choices=ROLES,default='other')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.username