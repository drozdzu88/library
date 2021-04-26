from django.contrib import admin
from .models import Author, Genere, Book, BookInstance

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Genere)

