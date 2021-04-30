from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genere


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(
        status='d').count()

    num_authors = Author.objects.count()
    num_generes = Genere.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_generes': num_generes,
    }

    return render(request, 'index.html', context=context)
