from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
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
    date_created = models.DateTimeField(verbose_name='date of Map Submission')
    medium = models.CharField(max_length=64,choices=MEDIUMS,default='other')
    tags = models.ManyToManyField('Tag',blank=True)
    approved = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    classic = models.BooleanField(default=False)
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
    def get_absolute_url(self):
        return "/showcase/sb/{0!s}".format(self.pk)

    def get_detail_url(self):
        return self.get_absolute_url() # remove later

    def get_storyboarder_url(self):
        return ["/showcase/author/{0!s}".format(a.pk) for a in self.storyboarder.all()]

    def get_mapset_url(self):
        return "https://osu.ppy.sh/s/{0!s}".format(self.set_id)

    def get_mapset_download_url(self):
        return "https://osu.ppy.sh/d/{0!s}".format(self.set_id)

    def get_mapset_thumbnail_url(self):
        return "//b.ppy.sh/thumb/{0!s}l.jpg".format(self.set_id)

    def get_mapset_card_url(self):
        return "//assets.ppy.sh//beatmaps/{0!s}/covers/card.jpg".format(self.set_id)

    def get_mapset_cover_url(self):
        return "//assets.ppy.sh//beatmaps/{0!s}/covers/cover.jpg".format(self.set_id)

    def get_video_url(self, embed=False):
        return ("https://youtu.be/" if not embed else "https://www.youtube.com/embed/") + self.video

    def get_embed_video_url(self):
        return self.get_video_url(embed=True)
    # endregion

    # region Utilities

    # maybe not useful after all
    def has_tag(self, internal_id):
        return any(internal_id == t.internal_id for t in self.tags.all())
    # endregion

    # region Ratings Related Fun

    def get_rating(self):
        sum = 0
        for t in self.tags.all():
            sum += t.rating
        return sum

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

    # region Regular Information
    username = models.CharField(max_length=64, verbose_name='username on osu!')
    profile_id = models.CharField(max_length=64,blank=True,default=0)
    title = models.CharField(max_length=64,blank=True,default='Storyboarder')
    role = models.CharField(max_length=64,choices=ROLES,default='other', verbose_name='server Role')
    description = models.TextField(blank=True)
    # endregion
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return r"/showcase/author/{0!s}".format(self.pk)

    def get_profile_url(self):
        return r'https://osu.ppy.sh/u/' + self.profile_id

    def get_avatar_url(self):
        return r'https://a.ppy.sh/' + self.profile_id

class Tag(models.Model):
    internal_id = models.SlugField(verbose_name="Internal ID")
    verbose_name = models.CharField(max_length=64,verbose_name="Tag Title")
    description = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(blank=True,default=0)

    def __str__(self):
        return self.verbose_name

    def get_icon_url(self):
        return r"/static/showcase/showcase-icons-exportable.svg#{0}".format(self.internal_id)

    def get_search_url(self):
        return r"/showcase/search?t={0}".format(self.internal_id)