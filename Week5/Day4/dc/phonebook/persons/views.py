from django.shortcuts import render, redirect
from .models import Person
from .forms import SearchForm


def search_person(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            return redirect('persons:search_results', search_query=search_query)
    else:
        form = SearchForm()
    return render(request, 'persons/search_person.html', {'form': form})


def search_results(request, search_query):
    persons = Person.objects.filter(name__icontains=search_query)
    return render(request, 'persons/search_results.html', {'persons': persons})
