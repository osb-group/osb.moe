# For custom template tags related to storyboarding showcase...

from django import template

register = template.Library()


@register.simple_tag
def display_medium_icon(m):
    medium = {
        'design':  'icon-osu-cookie',
        'osb':  'fa fa-file-text-o',
        'sgl':  'fa-file-code-o',
        'c':  'icon-c',
        'cplusplus': 'icon-cplusplus',
        'csharp': 'icon-csharp',
        'java': 'icon-java',
        'python': 'icon-python',
        'storybrew': 'fa fa-coffee',
        'other': 'Other'
    }
    return medium[m]