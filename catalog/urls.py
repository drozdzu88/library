from django.urls import path
from catalog.views import BookListView, BookDetailView

#app_name = 'catalog'
urlpatterns = [
    path('', BookListView.as_view(), name="books"),
    path('catalog/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
]
