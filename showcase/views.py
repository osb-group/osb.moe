from .models import Storyboard
from .models import Storyboarder
from .forms import StoryboardForm
from .forms import StoryboarderForm
from .forms import NewStoryboardForm
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView


class StoryboardListView(ListView):
    model = Storyboard

    def get_context_data(self, **kwargs):
        context = super(StoryboardListView, self).get_context_data(**kwargs)
        context['storyboard_list'] = Storyboard.objects.exclude(approved__exact=False).order_by('-date_created')
        return context


class StoryboardDetailView(DetailView):
    model = Storyboard

    def get_object(self):
        storyboard = super(StoryboardDetailView, self).get_object()
        return storyboard if storyboard.approved else get_object_or_404(Storyboard, pk=-1)


class StoryboarderDetailView(DetailView):
    model = Storyboarder

    def get_context_data(self, **kwargs):
        context = super(StoryboarderDetailView, self).get_context_data(**kwargs)
        context['storyboards'] = filter_by_author(context['storyboarder'])
        context['mediums'] = mediums_by_author(context['storyboarder'])
        return context

# Functions


def filter_by_author(request):
    return Storyboard.objects.filter(storyboarder=request).exclude(approved__exact=False).order_by('-date_created')


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


def edit_storyboarder(request, pk):
    storyboarder = get_object_or_404(Storyboarder, pk=pk)
    if request.method == "POST":
        form = StoryboarderForm(request.POST, instance=storyboarder)
        if form.is_valid():
            storyboarder = form.save(commit=False)
            storyboarder.save()
            return redirect(storyboarder.get_absolute_url())
    else:
        data = {'username': storyboarder.username, 'profile': storyboarder.profile,
                'description': storyboarder.description}
        form = StoryboarderForm(initial=data)
        return render(request, 'showcase/storyboarder_edit.html', {'form': form, 'storyboarder': storyboarder})


def new_storyboard(request):
    if request.method == "POST":
        form = NewStoryboardForm(request.POST)
        if form.is_valid():
            storyboard = form.save(commit=False)
            storyboard.date_added = timezone.now()
            storyboard.save()
            form.save_m2m()
            return redirect('StoryboardList')
    else:
        form = NewStoryboardForm()
    return render(request, 'showcase/storyboard_add.html', {'form': form})