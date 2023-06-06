from django.contrib.auth.models import AbstractUser
from django.db import models
from films.models import Film


class User(AbstractUser):
    favorite_films = models.ManyToManyField(
        Film, blank=True, related_name='favorited_by')
