# films/forms.py

from django import forms
from films.models import Film, Director
from films.models import Review


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('title', 'created_in_country',
                  'available_in_countries', 'category', 'director')


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ('first_name', 'last_name')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['film', 'review_text', 'rating']
