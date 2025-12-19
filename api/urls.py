from django.urls import path
from api.views import BookList, AuthorList

urlpatterns = [
    path('books/', BookList.as_view(), name="book-list"),
    path('authors/', AuthorList.as_view(), name="author-list"),
]