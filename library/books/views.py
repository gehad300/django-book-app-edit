from contextlib import redirect_stderr
from http.client import REQUEST_ENTITY_TOO_LARGE
from multiprocessing import context
from unicodedata import name
from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm


# Create your views here.


def getallbooks(request):
    context={
        "Books":Book.objects.all()
    }
    return render (request,'books/books.html',context=context)
def getonebook(request,book_id):
    book=Book.objects.get(id=book_id)
    context={
        "Book":book,
    }
    return render (request,'books/bookdetails.html',context=context)
def Add_Book(request):
    form=BookForm()
    if request.method=='POST':
       form=BookForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('All_Books')

    context={
        'form':form
    }
    return render (request,'books/create_book.html',context=context)


def update_Book(request,book_id):
        book=Book.objects.get(id=book_id)
        form=BookForm(instance=book)
        if request.method=='POST':
           form=BookForm(request.POST,request.FILES,instance=book)
           if form.is_valid():
             form.save()
             return redirect('All_Books')

        context={
            'form':form
                }        
        return render(request,'books/create_book.html',context)

def delete_book(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=='POST':
        book.delete()
        return redirect('All_Books')
    return render (request,'books/delete_form.html',{'object':book})