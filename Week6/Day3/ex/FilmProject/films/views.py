from django.urls import reverse_lazy
from django.views.generic import CreateView
from films.forms import FilmForm, DirectorForm
from .models import Film, Director
from django.views.generic import TemplateView
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from .models import Film


class HomePageView(TemplateView):
    template_name = 'home.html'


class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'film/addFilm.html'
    success_url = '/'


class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'director/addDirector.html'
    success_url = '/'


class FilmDeleteView(UserPassesTestMixin, generic.DeleteView):
    model = Film
    template_name = 'film/confirm_delete.html'
    success_url = reverse_lazy('films:homepage')

    def test_func(self):
        return self.request.user.is_superuser


class FavouriteFilmView(LoginRequiredMixin, View):
    def post(self, request, film_id):
        film = get_object_or_404(Film, id=film_id)
        user = request.user
        if film in user.favorite_films.all():
            user.favorite_films.remove(film)
        else:
            user.favorite_films.add(film)
        return HttpResponseRedirect(reverse('films:homepage'))


class FilmDetailView(generic.DetailView):
    model = Film
    template_name = 'film/film_detail.html'
    context_object_name = 'film'
