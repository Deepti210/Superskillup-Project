from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from books.models  import Book
import json 

@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books=Book.objects.all()
        books_data=[{"title":book.title,"author":book.author}for book in books]
        return JsonResponse(books_data,safe=False)


@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        book=Book.objects.create(title=data['title'],author=data['author'])
        return JsonResponse({"message":"Book added successfully"})