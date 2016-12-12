from django.shortcuts import render

from .models import Storyboard
from .models import Storyboarder
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView



class StoryboardListView(ListView):
    model = Storyboard

class StoryboardDetailView(DetailView):
    model = Storyboard

class StoryboarderDetailView(DetailView):
    model = Storyboarder

def search_request(request):
    storyboard_list = Storyboard.objects.order_by('date_created')
    if request.method == 'GET':
        search_terms = request.GET['s'].split()
        featured_flag = request.GET['f'] if 'f' in request.GET else False
        classic_flag = request.GET['c'] if 'c' in request.GET else False
        for s in search_terms:
            if storyboard_list:
                storyboard_list = storyboard_list.filter(Q(song__icontains=s) | Q(artist__icontains=s)
                                                         | Q(mapper__icontains=s) | Q(medium__icontains=s)
                                                         | Q(storyboarder__username__icontains=s))
        if featured_flag:
            storyboard_list = storyboard_list.filter(Q(featured=True))
        if classic_flag:
            storyboard_list = storyboard_list.filter(Q(classic=True))
        return render(request, 'showcase/storyboard_list.html', {'storyboard_list': storyboard_list})