from django.shortcuts import render, redirect
from .models import Book, Author 

# Create your views here.
def index(request):
    context = {
        'allbooks': Book.objects.all()
    }
    return render(request, "books.html", context)

def createBook(request):
    print(request.POST)
    Book.objects.create(title=request.POST['bookTitle'], 
    desc = request.POST['bookDesc'])
    return redirect('/')

def showBook(request, bookId):
    
    context = {
        'book':Book.objects.get(id=bookId),
        'allAuthors': Book.objects.get(id=bookId).authors.all()
    }
    return render(request, 'a_book.html', context)