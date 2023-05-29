from django.contrib import admin
from django.urls import path, include
from people_app.views import show_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/', show_list, name='people_list'),
]
