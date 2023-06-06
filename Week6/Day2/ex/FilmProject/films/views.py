from django.urls import reverse_lazy
from django.views.generic import CreateView
from films.forms import FilmForm, DirectorForm
from .models import Film, Director
from django.views.generic import TemplateView


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
