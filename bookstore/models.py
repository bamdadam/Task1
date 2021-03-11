from django.db import models


# Create your models here.


class Writer(models.Model):
    name = models.CharField(max_length=20)
    family_name = models.CharField(max_length=20)

    def __str__(self):
        return self.name + ' ' + self.family_name


class Book(models.Model):
    book_title = models.CharField(max_length=50)
    book_writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    book_date = models.DateField('date published')
    book_available = False

    def __str__(self):
        return self.book_title

    def is_available(self):
        return self.book_available

    def borrow_book(self):
        self.book_available = True

# class BookStore(models.Model):
#     book = models.OneToOneField(Book, on_delete=models.CASCADE)


class Borrow(models.Model):
    borrow_time = models.DateTimeField('date borrowed')
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(max_length=20)
    family_name = models.CharField(max_length=20)

    def __str__(self):
        return self.name + ' ' + self.family_name


class PrintBook:
    pass


class Publisher:
    pass
