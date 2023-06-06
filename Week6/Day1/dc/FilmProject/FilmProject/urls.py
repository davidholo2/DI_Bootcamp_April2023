from django.urls import path
from films.views import HomePageView, FilmCreateView, DirectorCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add-film/', FilmCreateView.as_view(), name='add_film'),
    path('add-director/', DirectorCreateView.as_view(), name='add_director'),

]
