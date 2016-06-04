from django.shortcuts import render

# Create your views here.
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from books.serializers import *
from .models import Book, Shelf, Author

#http GET http://localhost:8004/books/all/
@api_view(['GET'])
def all_books(request, **kwargs):
    books = Book.objects.all()

    serializers = BookSerializer(books, many=True)
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def add_book(request, **kwargs):
    title = request.data['title']
    if 'desc' in request.data:
        desc = request.data['desc']
    else:
        desc = ''

    book = Book.objects.create(
           title=title,
           desc=desc)

    #let's return the recent created Object in this View
    serializer = BookSerializer(book)
    return Response(serializer.data)
#http POST http://localhost:8004/books/author/add book_pk=2 author_pk=1
#http POST http://localhost:8004/books/author/add book_pk=2 author_pk=1
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def add_author_to_book(request, **kwargs):
    author = Author.objects.get(pk=request.data['author_pk'])
    book = Book.objects.get(pk=request.data['book_pk'])

    if author  not in book.authors.all():
        book.authors.add(author)
        book.save()

    #let's return the recent created Object in this View
    serializer = BookSerializer(book)
    return Response(serializer.data)
