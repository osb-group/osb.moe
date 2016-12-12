from django.shortcuts import render

from .models import Storyboard
from .models import Storyboarder
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone


class StoryboardListView(ListView):
    model = Storyboard

class StoryboardDetailView(DetailView):
    model = Storyboard

class StoryboarderDetailView(DetailView):
    model = Storyboarder


# Search view
# def search(request):
