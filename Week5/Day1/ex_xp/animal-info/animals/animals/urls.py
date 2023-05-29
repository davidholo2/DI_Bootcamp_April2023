from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('family/<str:family_name>/', family_view, name='family'),
    path('animal/<int:animal_id>/', animal_view, name='animal'),
]
