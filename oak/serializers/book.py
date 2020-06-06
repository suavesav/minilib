from oak.models import Book
from rest_framework import serializers

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        # Add author
        fields = ['gapi_id', 'title', 'cover']
