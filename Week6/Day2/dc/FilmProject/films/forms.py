# films/forms.py

from django import forms
from films.models import Film, Director
from .models import Review


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
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }

    def save(self, commit=True, user=None):
        review = super().save(commit=False)
        if user:
            review.review_author = user
        if commit:
            review.save()
        return review
