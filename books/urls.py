from django.urls import path
from books.views import book_list,add_book

urlpatterns=[
    path('books/',book_list,name='book-list'),
    path('add-book/',add_book,name='add-book'),
]