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

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name


class Book(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gapi_id = models.CharField(max_length=12, default=None, null=True, db_index=True, unique=True)
    title = models.CharField(max_length=1024)
    author = models.ManyToManyField(Author, related_name='books')
    cover = models.URLField(max_length=2048)

    def __str__(self):
        return self.title


class Bookshelf(BaseModel):
    # User-Book Mapping
    user = models.OneToOneField(User, db_index=True, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, default=None, related_name='bookshelves')
