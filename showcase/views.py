from .models import Storyboard
from .models import Storyboarder
from .forms import StoryboardForm
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView


class StoryboardListView(ListView):
    model = Storyboard

    def get_context_data(self, **kwargs):
        context = super(StoryboardListView, self).get_context_data(**kwargs)
        context['storyboard_list'] = Storyboard.objects.order_by('-date_created')
        return context


class StoryboardDetailView(DetailView):
    model = Storyboard


class StoryboarderDetailView(DetailView):
    model = Storyboarder

    def get_context_data(self, **kwargs):
        context = super(StoryboarderDetailView, self).get_context_data(**kwargs)
        context['storyboards'] = filter_by_author(context['storyboarder'])
        context['mediums'] = mediums_by_author(context['storyboarder'])
        return context

# Functions


def filter_by_author(request):
    return Storyboard.objects.filter(storyboarder=request).order_by('-date_created')


def mediums_by_author(request):
    sb_list = filter_by_author(request)
    medium_set = set()
    for s in sb_list:
        medium_set.add(s.medium)
    return list(medium_set)


def search_request(request):
    storyboard_list = Storyboard.objects.order_by('-date_created')
    if request.method == 'GET':
        search_terms = request.GET['s'].split()
        featured_flag = request.GET['f'] if 'f' in request.GET else False
        classic_flag = request.GET['c'] if 'c' in request.GET else False
        for s in search_terms:
            if storyboard_list:
                storyboard_list = storyboard_list.filter(Q(song__icontains=s) | Q(artist__icontains=s)
                                                         | Q(mapper__icontains=s) | Q(medium__icontains=s)
                                                         )
        if featured_flag:
            storyboard_list = storyboard_list.filter(Q(featured=True))
        if classic_flag:
            storyboard_list = storyboard_list.filter(Q(classic=True))
        return render(request, 'showcase/storyboard_list.html', {'storyboard_list': storyboard_list})


def edit_storyboard(request, pk):
    storyboard = get_object_or_404(Storyboard, pk=pk)
    if request.method == "POST":
        form = StoryboardForm(request.POST, instance=storyboard)
        if form.is_valid():
            storyboard = form.save(commit=False)
            storyboard.save()
            return redirect(storyboard.get_absolute_url())
    else:
        data = {'song': storyboard.song, 'artist': storyboard.artist, 'set_id': storyboard.set_id,
                'medium': storyboard.medium, 'comments': storyboard.comments,
                'description': storyboard.description, 'video': storyboard.video}
        form = StoryboardForm(initial=data)
    return render(request, 'showcase/storyboard_edit.html', {'form': form, 'storyboard': storyboard})