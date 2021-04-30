
from django.views import generic
from catalog.models import Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 20


class BookDetailView(generic.DetailView):
    model = Book
