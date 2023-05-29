from django.urls import path
from . import views

urlpatterns = [
    path('family/<int:family_id>/', views.family_view, name='family_view'),
    path('animal/<int:animal_id>/', views.animal_view, name='animal_view'),
    path('animals/', views.animals_list, name='animals_list'),
]
