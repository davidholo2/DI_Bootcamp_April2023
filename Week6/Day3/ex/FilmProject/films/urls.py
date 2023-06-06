from django.urls import path
from .views import FilmDeleteView
from .views import FavouriteFilmView

app_name = 'films'

urlpatterns = [
    path('film/delete/<int:pk>/', FilmDeleteView.as_view(), name='delete_film'),
    path('film/favourite/<int:film_id>/',
         FavouriteFilmView.as_view(), name='favourite_film'),
    path('film/detail/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),


]
