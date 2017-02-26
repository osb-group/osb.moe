from django.conf.urls import url
from showcase.views import search_request, edit_storyboard, edit_storyboarder, new_storyboard
from showcase.views import StoryboardListView, StoryboardDetailView, StoryboarderDetailView, StoryboardLeaderboardView

urlpatterns = [
    url(r'^$', StoryboardListView.as_view(), name='StoryboardList'),
    url(r'^search', search_request),
    url(r'^sb/(?P<pk>[0-9]+)/$', StoryboardDetailView.as_view(), name='StoryboardDetail'),
    url(r'^author/(?P<pk>[0-9]+)/$', StoryboarderDetailView.as_view(), name='StoryboarderDetail'),
    url(r'sb/(?P<pk>[0-9]+)/edit', edit_storyboard),
    url(r'^author/(?P<pk>[0-9]+)/edit', edit_storyboarder),
    url(r'^sb/new', new_storyboard),
    url(r'leaderboard/$', StoryboardLeaderboardView.as_view(), name='StoryboardLeaderboard'),
]