from django.urls import path
from . import views

app_name = 'persons'

urlpatterns = [
    path('', views.search_person, name='search_person'),
    path('name/', views.search_by_name, name='search_by_name'),
    path('phonenumber/', views.search_by_phonenumber,
         name='search_by_phonenumber'),
]
