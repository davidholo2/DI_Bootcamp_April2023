from django.shortcuts import render, redirect
from .models import Gif, Category
from .forms import GifForm, CategoryForm


def homepage(request):
    gifs = Gif.objects.all()
    return render(request, 'gifs/homepage.html', {'gifs': gifs})


def add_gif(request):
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = GifForm()
    return render(request, 'gifs/add_gif.html', {'form': form})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request, 'gifs/add_category.html', {'form': form})


def category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    gifs = category.gifs.all()
    return render(request, 'gifs/category.html', {'category': category, 'gifs': gifs})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'gifs/categories.html', {'categories': categories})


def gif_view(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    return render(request, 'gifs/gif.html', {'gif': gif})


def increment_likes(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    gif.likes += 1
    gif.save()
    return redirect('gif_view', gif_id=gif_id)


def decrement_likes(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    gif.likes -= 1
    gif.save()
    return redirect('gif_view', gif_id=gif_id)


def positive_likes(request):
    gifs = Gif.objects.filter(likes__gt=0).order_by('-likes')
    return render(request, 'gifs/positive_likes.html', {'gifs': gifs})
