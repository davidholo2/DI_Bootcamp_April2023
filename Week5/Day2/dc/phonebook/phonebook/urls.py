from django.contrib import admin
from django.urls import path
from directory.views import phone_number_view, name_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('persons/phonenumber/', phone_number_view, name='phone_number_view'),
    path('persons/name/', name_view, name='name_view'),
]
