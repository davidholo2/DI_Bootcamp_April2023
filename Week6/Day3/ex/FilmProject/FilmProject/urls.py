from django.urls import path
from films.views import HomePageView, FilmCreateView, DirectorCreateView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add-film/', FilmCreateView.as_view(), name='add_film'),
    path('add-director/', DirectorCreateView.as_view(), name='add_director'),
    path('admin/', admin.site.urls),
    path('', include('films.urls', namespace='films')),
    path('accounts/', include('accounts.urls', namespace='accounts')),

]
