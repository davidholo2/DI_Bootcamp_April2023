from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Rental, Customer, Vehicle


class RentalListView(ListView):
    model = Rental
    template_name = 'rent/rental_list.html'


class RentalDetailView(DetailView):
    model = Rental
    template_name = 'rent/rental_detail.html'


class RentalCreateView(CreateView):
    model = Rental
    fields = '__all__'
    template_name = 'rent/rental_add.html'


class CustomerListView(ListView):
    model = Customer
    template_name = 'rent/customer_list.html'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'rent/customer_detail.html'


class CustomerCreateView(CreateView):
    model = Customer
    fields = '__all__'
    template_name = 'rent/customer_add.html'


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'rent/vehicle_list.html'


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'rent/vehicle_detail.html'


class VehicleCreateView(CreateView):
    model = Vehicle
    fields = '__all__'
    template_name = 'rent/vehicle_add.html'
