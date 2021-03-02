from django.db import models

# Create your models here.


class Writer(models.model):
    name = models.CharField(max_length=20)
    family_name = models.CharField(max_length=20)


class Book(models.model):
    book_title = models.CharField(max_length=200)
    book_writer = models.ForeignKey(Writer, on_delete=models.CASCADE())
