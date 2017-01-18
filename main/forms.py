from django import forms

class OsuUserVerificationForm(forms.Form):
    osu_username = forms.CharField(abel='osu! Username', max_length='32')
    match_id = forms.IntegerField(label='Multiplayer Match ID', max_length='32')
