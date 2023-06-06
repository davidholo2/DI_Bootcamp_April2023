from django.urls import path
from films.views import HomePageView, FilmCreateView, DirectorCreateView
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('add-film/', FilmCreateView.as_view(), name='add_film'),
    path('add-director/', DirectorCreateView.as_view(), name='add_director'),
    path('accounts/', include('accounts.urls', namespace='accounts')),

]
