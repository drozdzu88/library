from django.db import models
from django.urls import reverse
import uuid


class Genere(models.Model):
    """Model representing a book genere."""
    name = models.CharField(max_length=200, help_text='Podaj gatunek książki '
                                                      'np. Thriller. ')

    def __str__(self):
        return self.name


class Language(models.Model):
    """Model representing a book language e.g. English"""
    name = models.CharField(max_length=200, help_text='Wpisz w jakim języku '
                                                      'jest napisana ksiażka')

    def __str__(self):
        return self.name


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Book(models.Model):
    """Model representing a book, but not a specific copy of book"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Podaj krótki opis '
                                                          'książki.')
    num_of_pages = models.IntegerField(null=True, blank=False)
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 znaków <a href"https://pl.wikipedia.org/wiki/Mi%C4%99dzynarodowy_znormalizowany_numer_ksi%C4%85%C5%BCki">ISBN Wiki</a>')
    genere = models.ManyToManyField(Genere, help_text='Wybierz gatunek książki')
    cover = models.ImageField(upload_to='catalog/%Y/%m/%d', blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genere(self):
        """Create a string for the Genere. This is required to display gener
        in Admin"""
        return ', '.join(genere.name for genere in self.genere.all()[:3])

    display_genere.short_description = 'Genere'


class BookInstance(models.Model):
    """Model representing a specific copy of book (i.e. that can be borrowed)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unikalny identyfikator danego '
                                    'egzemplarza książki w całej bibliotece')
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('k', 'Konserwacja'),
        ('w', 'Wypożyczona'),
        ('d', 'Dostępna'),
        ('z', 'Zarezerwowana'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True,
                              default='k', help_text='Dostępność książki')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'
