
from django.views import generic
from catalog.models import Book, Author


class BookListView(generic.ListView):
    model = Book
    paginate_by = 20


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 20


class AuthorDetailView(generic.DetailView):
    model = Author
