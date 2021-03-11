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
        writer = Writer.objects.get(id=kwargs['id'])
        try:
            book_param = json.loads(request.body)
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
        book = Book.objects.create(book_writer=writer,
                                   book_title=book_title,
                                   book_date=book_date)
        return HttpResponse(book)
    else:
        raise ValidationError('invalid request')


def list_books(request):
    if request.method == 'GET':
        book_list = Book.objects.all()
        return HttpResponse('\n'.join(str(i) for i in book_list))
    else:
        raise ValidationError('invalid request')


def book_publish_dates(request, **kwargs):
    if request.method == 'GET':
        try:
            book_param = json.loads(request.body)
            try:
                book = Book.objects.get(book_title=book_param['book_title'],
                                        book_date=book_param['book_date'],
                                        book_writer=book_param['book_writer'])
                return HttpResponse(book)
            except:
                raise ValidationError("book not found")
        except(TypeError, KeyError) as e:
            return HttpResponse(traceback.print_exc())

    else:
        raise ValidationError('invalid request')


def writers_books(request):
    pass
