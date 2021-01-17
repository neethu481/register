from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from django.contrib import messages
from .forms import UserSignupForm



# Create your views here.


def book_list(request):
    context = {'book_list': Book.objects.all()}
    return render(request, "book_register/book_list.html", context)


def book_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(instance=book)
        return render(request, "book_register/book_form.html", {'form': form})
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('/list')


def book_delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('/list')

