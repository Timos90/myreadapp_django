from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from apps.core.constants import BOOK_CATEGORY, BOOK_FORMAT
from .forms import PostBookForm

# Create your views here.
def book_detail(request, isbn):
    book = models.Book.objects.get(pk=isbn)
    # authors = ", ".join([str(author) for author in book.authors.all()])
    # tags = ", ".join([str(tag) for tag in book.tags.all()])
    book.category = BOOK_CATEGORY.get(book.category, "category")
    book.book_format = BOOK_FORMAT.get(book.book_format, "book_format")

      # Set the maximum viewed books
    max_viewed_books: int = 5

    # Get the current stored session
    viewed_books: list = request.session.get('viewed_books', [])

    #Create the data to be stored ins the session
    viewed_book: list[str] = [book.isbn, book.title]

    # Remove if exists already
    if viewed_book in viewed_books:
        viewed_books.remove(viewed_book)

    # Insert the viewed book in index 0
    viewed_books.insert(0, viewed_book)

    # Get the limit
    viewed_books = viewed_books[:max_viewed_books]

    # Replace in the sesion
    request.session['viewed_books'] = viewed_books

    context = {
        'book': book,
    }

    return render(request, 'book_details.html', context)

# def book_post(request):
#     # breakpoint()
#     return render(request, 'post.html')

def book_post(request):
    # Get our form in the two states:
    # - pre-submit
            # -http method: 'GET'
    # - post-submit
            # -http method: 'POST'
    if request.method == 'GET':
        form = PostBookForm()
        context = {"form":form}
        return render(
            request,
            'book_post.html',
            context
        )
    elif request.method == 'POST':
        data = request.POST
        form = PostBookForm(data)

        # validation
        if form.is_valid():
            data = form.cleaned_data
            # TODO: Save to database
            # TODO: Redirect to homepage

            book = models.Book(
                isbn=data['isbn'],
                title=data['title'],
                page_count=data['pages'],
                description=data['description'],
                category=data['category'],
                published_date = data['published_year'],
                publisher=data['publisher'],
                language=data['language'],
                edition=data['edition'],
                book_format=data['book_format']
            )

            book.save()

            book.tags.set(data['tags'])
            book.save()

            return redirect('myread-urls:home-page')
