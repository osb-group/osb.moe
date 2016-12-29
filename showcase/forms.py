from django import forms

from .models import Storyboard

class StoryboardForm(forms.ModelForm):

    class Meta:
        model = Storyboard
        fields = ('song', 'artist', 'set_id', 'medium', 'comments', 'description', 'video',)