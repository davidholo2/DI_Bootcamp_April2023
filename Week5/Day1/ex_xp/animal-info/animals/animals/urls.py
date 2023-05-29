from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('family/<fam_id>', families),
    path('animal/<animal_id>', animals)
]
