from django.shortcuts import render
from bookstore.models import Book, Author

def books_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'author_detail.html', {'author': author})
