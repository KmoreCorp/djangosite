from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name ='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/',views.LoanedBooksByUserListView.as_view() , name = 'my-borrowed'),
    path('allloaedbooks/',views.LoanedAllBooks.as_view() , name = 'all-loaned'),
]