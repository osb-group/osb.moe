from django.conf.urls import url
from showcase.views import search_request
from showcase.views import edit_storyboard
from showcase.views import StoryboardListView
from showcase.views import StoryboardDetailView
from showcase.views import StoryboarderDetailView


urlpatterns = [
    url(r'^$', StoryboardListView.as_view()),
    url(r'^search', search_request),
    url(r'sb/(?P<pk>[0-9]+)/edit', edit_storyboard),
    url(r'^sb/(?P<pk>[0-9]+)/$', StoryboardDetailView.as_view(), name='StoryboardDetail'),
    url(r'^author/(?P<pk>[0-9]+)$', StoryboarderDetailView.as_view(), name='StoryboarderDetail'),
]