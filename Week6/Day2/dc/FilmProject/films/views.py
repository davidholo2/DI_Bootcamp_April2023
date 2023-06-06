from django.urls import reverse_lazy
from django.views.generic import CreateView
from films.forms import FilmForm, DirectorForm
from .models import Film, Director
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from .forms import ReviewForm
from .models import Review
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


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'films/addReview.html'

    def form_valid(self, form):
        film = get_object_or_404(Film, pk=self.kwargs['pk'])
        return form.save(user=self.request.user, commit=True)
