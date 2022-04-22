from unicodedata import name
from django.shortcuts import render

from books.models import Book
from .models import author

# Create your views here.
def getoneauthor(request,author_id):
    book_author = Book.objects.filter(author_id=author_id).values()
    print(book_author)
    context={
        "Book_author":book_author,
        "author_name":author.objects.get(id=author_id)
    }
    return render (request,'author/autherdetails.html',context=context)
    