from django.contrib import admin

from .models import Storyboard
from .models import Storyboarder


class StoryboardAdmin(admin.ModelAdmin):
    list_display = ('song', 'artist', 'set_id', 'storyboarder', 'date_added', 'date_created', 'medium', 'featured', 'classic')
    list_filter = ['date_added', 'date_created']
    search_fields = ['song', 'artist']

class StoryboarderAdmin(admin.ModelAdmin):
    list_display = ('username', 'profile')
    search_fields = ['username']


admin.site.register(Storyboard, StoryboardAdmin)
admin.site.register(Storyboarder, StoryboarderAdmin)