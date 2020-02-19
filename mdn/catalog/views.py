from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre
from django.views import generic
#登录用户验证，相当于@login_required
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


def index(request):
    # Generate counts of some of the main objects

    num_books = Book.objects.all().count()

    ## 用session来记录访问该用户访问次数，第一次，加入0
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1


    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_books_keyword = Book.objects.filter(title__contains='失落').count()




    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
        'num_genres' : num_genres,
        'num_books_keyword' : num_books_keyword,
        'num_visits' : num_visits
    }

    return render(request, 'index.html', context = context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """docstring for LoanedBooksByUserListView"""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class LoanedAllBooks(PermissionRequiredMixin,generic.ListView):
    permission_required = ('catalog.can_mark_returned',)
    model = BookInstance
    paginate_by = 10
    template_name = 'catalog/bookinstance_all_loaned.html'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o')