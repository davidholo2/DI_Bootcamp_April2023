from django.contrib import admin
from django.urls import path
from gifs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('add_gif/', views.add_gif, name='add_gif'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<int:category_id>/',
         views.category_view, name='category_view'),
    path('categories/', views.categories, name='categories'),
    path('gif/<int:gif_id>/', views.gif_view, name='gif_view'),
]
