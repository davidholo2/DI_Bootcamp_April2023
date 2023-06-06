from django.urls import reverse_lazy
from django.views.generic import CreateView
from films.forms import FilmForm, DirectorForm, ReviewForm
from .models import Film, Director
from django.views.generic import TemplateView
from .models import Film, Director, Review


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


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/addReview.html'
    success_url = '/'
