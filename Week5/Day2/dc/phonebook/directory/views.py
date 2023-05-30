from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def phone_number_view(request):
    if 'phone_number' in request.GET:
        phone_number = request.GET['phone_number']
        try:
            person = Person.objects.get(phone_number=phone_number)
            return render(request, 'person_info.html', {'person': person})
        except Person.DoesNotExist:
            return HttpResponse("No person found with the provided phone number.")
    else:
        return HttpResponse("Please provide a phone number.")

def name_view(request):
    if 'name' in request.GET:
        name = request.GET['name']
        try:
            person = Person.objects.get(name=name)
            return render(request, 'person_info.html', {'person': person})
        except Person.DoesNotExist:
            return HttpResponse("No person found with the provided name.")
    else:
        return HttpResponse("Please provide a name.")
