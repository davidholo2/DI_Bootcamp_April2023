from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def todo_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
    else:
        form = TodoForm()

    return render(request, 'todo/todo_form.html', {'form': form})


def display_todos(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})
