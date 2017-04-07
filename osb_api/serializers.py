from rest_framework import serializers
from showcase.models import Storyboard, Storyboarder
from django.contrib.auth.models import User

class StoryboarderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storyboarder
        fields = ('username', 'profile_id')

class StoryboardSerializer(serializers.ModelSerializer):
    storyboarder = StoryboarderSerializer(many=True, read_only=True)

    tags = serializers.SlugRelatedField(
        slug_field='verbose_name',
        many=True,
        read_only=True
    )

    class Meta:
        model = Storyboard
        fields = ('song', 'artist', 'set_id',
                  'storyboarder', 'mapper',
                  'date_added', 'date_created',
                  'medium', 'tags',
                  'video')