from django.views import generic as g
from django.urls import reverse_lazy, reverse
from .forms import SeasonForm, ChapterForm, DragaDataForm
from season import models as m


class SeasonListView(g.ListView):
    model = m.Season
    template_name = 'season/season_list.html'
    context_object_name = 'seasons'


class SeasonCreateView(g.edit.CreateView):
    model = m.Season
    form_class = SeasonForm
    template_name = 'season/season_create.html'
    success_url = reverse_lazy('season_list')


class ChapterListView(g.ListView):
    template_name = 'season/chapter_list.html'
    context_object_name = 'chapters'

    def get_queryset(self):
        return m.Chapter.objects.filter(season_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['season'] = m.Season.objects.get(pk=self.kwargs['pk'])
        return context


class ChapterCreateView(g.edit.CreateView):
    model = m.Chapter
    form_class = ChapterForm
    template_name = 'season/chapter_create.html'

    def form_valid(self, form):
        form.instance.season_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('chapter_list', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['season'] = m.Season.objects.get(pk=self.kwargs['pk'])
        return context


class DragaDataCreateView(g.edit.CreateView):
    model = m.DragaSeasonenData
    form_class = DragaDataForm
    template_name = 'season/draga_data_create.html'

    def form_valid(self, form):
        form.instance.season_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('chapter_list', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['season'] = m.Season.objects.get(pk=self.kwargs['pk'])
        return context

