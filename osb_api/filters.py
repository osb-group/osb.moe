from django_filters import rest_framework as filters
from django.db import models
from showcase.models import Storyboard, Storyboarder, Tag

class StoryboardFilter(filters.FilterSet):

    storyboarder = filters.ModelMultipleChoiceFilter(
        name='storyboarder__username',
        to_field_name='username',
        queryset=Storyboarder.objects.all(),
        conjoined=True,
    )

    tags = filters.ModelMultipleChoiceFilter(
        name='tags__internal_id',
        to_field_name='internal_id',
        queryset=Tag.objects.all(),
        conjoined=True,
    )

    class Meta:
        model = Storyboard

        fields = ['song', 'artist', 'set_id',
                  'storyboarder', 'mapper',
                  'date_added', 'date_created',
                  'medium', 'tags']

        filter_overrides = {
            models.CharField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                }
            }
        }
