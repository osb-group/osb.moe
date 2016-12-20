# For custom template tags related to storyboarding showcase...

from django import template
from ..models import Storyboard
from ..models import Storyboarder

register = template.Library()

# Utility-based template tags


@register.simple_tag
def display_medium_icon(m):
    medium = {
        'design':  'icon-osu-cookie',
        'osb':  'fa fa-file-text-o',
        'sgl':  'fa fa-file-code-o',
        'c':  'icon-c',
        'cplusplus': 'icon-cplusplus',
        'csharp': 'icon-csharp',
        'java': 'icon-java',
        'python': 'icon-python',
        'storybrew': 'fa fa-coffee',
        'other': 'Other'
    }
    return medium[m]

# List tags

@register.simple_tag
def get_storyboards():
    return Storyboard.objects.order_by('-date_created')

@register.simple_tag
def get_storyboarders():
    return Storyboarder.objects.order_by('username')

# Filter tags

# Template-rendering tags


@register.inclusion_tag('storyboard_card.html')
def show_sb_card(storyboard):
    return {'s': storyboard}


@register.inclusion_tag('storyboarder_card.html')
def show_sber_card(sb):
    return {'s': sb}