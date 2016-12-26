from __future__ import unicode_literals
import operator

from django.db import models
from django.db.models import Q
from photologue.models import Gallery


class Storyboard(models.Model):
    # region Constants
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
    # endregion

    # region Sortables
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
    # endregion

    # region Non-sortables
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True)
    comments = models.TextField(blank=True, verbose_name="author's comments")
    description = models.TextField(blank=True)
    video = models.CharField(blank=True, max_length=16, verbose_name='youTube Video ID')
    # endregion

    def __str__(self):
        return "%s - %s" % (self.artist, self.song)

    # region Display URLs
    def get_detail_url(self):
        return "/showcase/sb/{0!s}".format(self.pk)

    def get_storyboarder_url(self):
        return ["/showcase/author/{0!s}".format(a.pk) for a in self.storyboarder.all()]

    def get_mapset_url(self):
        return "https://osu.ppy.sh/s/{0!s}".format(self.set_id)

    def get_mapset_download_url(self):
        return "https://osu.ppy.sh/d/{0!s}".format(self.set_id)

    def get_mapset_thumbnail_url(self):
        return "//b.ppy.sh/thumb/{0!s}l.jpg".format(self.set_id)

    def get_mapset_cover_url(self):
        return "//assets.ppy.sh//beatmaps/{{0!s}}/covers/card.jpg".format(self.set_id)

    def get_video_url(self, embed=False):
        return ("https://youtu.be/" if not embed else "https://www.youtube.com/embed/") + self.video

    def get_embed_video_url(self):
        return self.get_video_url(embed=True)
    # endregion


class Storyboarder(models.Model):
    # region Constants
    ROLES = (
        ('owner', 'Server Owner'),
        ('mentor', 'Mentor'),
        ('storyboarder', 'Storyboarder'),
        ('apprentice', 'Apprentice'),
        ('other', 'Other'),
    )
    # endregion

    username = models.CharField(max_length=64)
    avatar = models.ImageField(blank=True, upload_to='a')
    profile = models.URLField(blank=True)
    title = models.CharField(max_length=64,blank=True,default='Storyboarder')
    role = models.CharField(max_length=64,choices=ROLES,default='other')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.username