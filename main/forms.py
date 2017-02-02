from django import forms

class OsuUserVerificationForm(forms.Form):
    osu_username = forms.CharField(label='osu! Username', max_length='32')
    match_id = forms.IntegerField(label='Multiplayer Match ID', min_value=0, initial=0)
