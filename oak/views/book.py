from oak.models import Book
from rest_framework import viewsets
from oak.serializers.book import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
