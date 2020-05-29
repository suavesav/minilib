from django.contrib.auth.models import User
from django.db import models
import uuid

class BaseModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)


class Author(BaseModel):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)


class Book(BaseModel):
    gapi_id = models.CharField(max_length=12, default=None, null=True, db_index=True, unique=True)
    title = models.CharField(max_length=1024)
    author = models.ManyToManyField(Author, related_name='books')
    cover = models.URLField(max_length=2048)


class Bookshelf(BaseModel):
    # User-Book Mapping
    user = models.OneToOneField(User, db_index=True, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, default=None, null=True, related_name='bookshelves')
