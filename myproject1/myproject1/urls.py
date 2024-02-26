from django.urls import path
from bookstore import views

urlpatterns = [
    path('', views.authors_list, name='authors_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('books/', views.books_list, name='books_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
]