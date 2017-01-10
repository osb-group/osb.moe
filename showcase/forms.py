from django import forms
from django.forms.widgets import DateTimeInput
from .models import Storyboard
from .models import Storyboarder

class StoryboardForm(forms.ModelForm):
    class Meta:
        model = Storyboard
        fields = ('song', 'artist', 'set_id', 'medium', 'comments', 'description', 'video',)

class NewStoryboardForm(forms.ModelForm):
    class Meta:
        model = Storyboard
        fields = ('song', 'artist', 'set_id', 'date_created', 'mapper', 'storyboarder', 'medium', 'comments', 'description',
                  'video',)
        widgets = {'date_created': DateTimeInput}


class StoryboarderForm(forms.ModelForm):
    class Meta:
        model = Storyboarder
        fields = ('username', 'profile_id', 'description')