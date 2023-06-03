from django.urls import path
from . import views

app_name = 'rent'

urlpatterns = [
    path('rental/', views.RentalListView.as_view(), name='rental_list'),
    path('rental/<int:pk>/', views.RentalDetailView.as_view(), name='rental_detail'),
    path('rental/add/', views.RentalCreateView.as_view(), name='rental_add'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(),
         name='customer_detail'),
    path('customer/', views.CustomerListView.as_view(), name='customer_list'),
    path('customer/add/', views.CustomerCreateView.as_view(), name='customer_add'),
    path('vehicle/', views.VehicleListView.as_view(), name='vehicle_list'),
    path('vehicle/<int:pk>/', views.VehicleDetailView.as_view(),
         name='vehicle_detail'),
    path('vehicle/add/', views.VehicleCreateView.as_view(), name='vehicle_add'),
]
