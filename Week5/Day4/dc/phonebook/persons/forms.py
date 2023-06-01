from django import forms


class SearchForm(forms.Form):
    # Define form fields here
    search_field = forms.CharField(max_length=100)
