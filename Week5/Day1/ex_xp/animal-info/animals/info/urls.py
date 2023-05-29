from django.urls import path
from .views import family_view, animal_view

app_name = 'info'

urlpatterns = [
    path('family/<int:family_id>/', family_view, name='family'),
    path('animal/<int:animal_id>/', animal_view, name='animal'),
]
