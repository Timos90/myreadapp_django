from django.db import models
from django.contrib.postgres.fields import ArrayField # Postgresql specific

# Create your models here.

class BookManager(models.Manager):
    # self = Book.objects
    def get_books_by_tags(self, *tags):
        return self.filter(tags__name__in=tags)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class BookAuthor(models.Model):
    BOOK_AUTHOR_ROLE = {
        'author': 'Author',
        'co_author': 'Co_Author',
        'editor': 'Editor'
    }
    book = models.ForeignKey('book.book', on_delete=models.CASCADE)
    author = models.ForeignKey('book.Author', on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices= BOOK_AUTHOR_ROLE, default='author')

    def __str__(self) -> str:
        return f'{self.author} {self.role} {self.book}'

class Book(models.Model):
    BOOK_CATEGORY = {
        "pr": "programming",
        "ar": "art",
        "hi": "history",
        "po": "politics",
        "ot": "others"
    }
    BOOK_FORMAT = {
        "eb": "ebook",
        "hc": "hardcover"
    }
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    page_count = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=2, choices=BOOK_CATEGORY, default='pr')
    published_date = models.IntegerField()
    publisher = models.CharField(max_length=50)
    #authors = ArrayField(ArrayField(models.CharField(max_length=50)))
    authors = models.ManyToManyField('book.Author',related_name='book', through='book.BookAuthor')
    language = models.CharField(max_length=50)
    edition = models.SmallIntegerField(null=True, blank=True)
    book_format = models.CharField(max_length=2, choices=BOOK_FORMAT, default='eb')
    tags = models.ManyToManyField('book.Tag', related_name='book')

    # Override objects with now Manager
    objects = BookManager()

    # @classmethod
    # class get_books_by_tags(cls, *tags):
    #     return cls.objects.filter(tags__name__in=tags)


    @property
    def short_des(self):
        return f'{self.description[:30]}...'

    def __str__(self) ->str:
        return f"{self.title}({self.published_date})"
    