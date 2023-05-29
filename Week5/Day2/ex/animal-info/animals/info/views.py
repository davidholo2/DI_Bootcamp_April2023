from django.shortcuts import render
from .models import Family, Animal


def family_view(request, family_id):
    family = Family.objects.get(pk=family_id)
    animals = Animal.objects.filter(family=family)
    return render(request, 'family.html', {'family': family, 'animals': animals})


def animal_view(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return render(request, 'animal.html', {'animal': animal})


def animals_list(request):
    animals = Animal.objects.all()
    return render(request, 'animals_list.html', {'animals': animals})
