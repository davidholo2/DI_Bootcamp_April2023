from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.people_list, name='people_list'),
]
