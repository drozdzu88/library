from django.urls import path
from catalog.views import BookListView, BookDetailView, AuthorListView, \
    AuthorDetailView

#app_name = 'catalog'
urlpatterns = [
    path('', BookListView.as_view(), name="books"),
    path('catalog/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('author/', AuthorListView.as_view(), name="authors"),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name="author-detail"),
]
