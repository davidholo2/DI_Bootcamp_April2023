from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
