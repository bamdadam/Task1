from django.urls import path, include
from django.contrib import admin
from bookstore import views
urlpatterns = [
    path('createbook/<int:id>/', views.make_book, name='make book'),
    path('listbooks/', views.list_books, name='list books'),
    path('bookpublish/<int:id>/', views.book_publish_dates, name='book publish dates'),
]
