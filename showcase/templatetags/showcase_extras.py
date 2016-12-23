# For custom template tags related to storyboarding showcase...

from django import template
from ..models import Storyboard
from ..models import Storyboarder
import random

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

@register.inclusion_tag('storyboard_carousel.html')
def show_screenshot_carousel():
    sb_list = set()
    featured_sb_list = Storyboard.objects.filter(featured=True)
    nonfeatured_sb_list = Storyboard.objects.filter(featured=False)

    while len(sb_list) < 3:
        if random.randint(1, 100) > 30:
            sb_list.add(random.choice(featured_sb_list))
        else:
            sb_list.add(random.choice(nonfeatured_sb_list))

    carousel_gallery = []
    for sb in list(sb_list):
        if sb.gallery.public():
            carousel_gallery.append(random.choice(sb.gallery.public()))

    sb_carousel = zip(list(sb_list), carousel_gallery)

    return {'storyboards': sb_carousel}