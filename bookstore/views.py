import traceback
from datetime import datetime

from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponse, Http404
from bookstore.models import Writer, Book
import json


# Create your views here.

def make_book(request, **kwargs):
    if request.method == 'POST':
        # Writer.objects.get(name=kwargs['name'], family_name=kwargs['family_name'])
        writer = Writer.objects.get(id=kwargs['id'])
        # print(writer)
        try:
            book_param = json.loads(request.body)
            # print(book_param)
            if len(book_param['book_title']) <= 20:
                book_title = book_param['book_title']
                print(book_title)
            else:
                raise ValidationError('book title len must be less than equal to 20')
            try:
                datetime.strptime(book_param['book_date'], "%Y-%m-%d")
                book_date = book_param['book_date']
                print(book_date)
            except:
                raise ValidationError('book date should be a valid date')
        except (TypeError, KeyError) as e:
            return HttpResponse(traceback.print_exc())
        book = Book.objects.create(book_writer=writer, book_title=book_title, book_date=book_date)
        return HttpResponse(book)
    else:
        raise ValidationError('invalid request')


def list_books(request):
    return HttpResponse(Book.objects.all())


def book_publish_dates(request):
    pass


def writers_books(request):
    pass
