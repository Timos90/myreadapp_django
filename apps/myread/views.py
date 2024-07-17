# Inbuilt imports

# Framework imports
from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count

# Custom import
from . import utils
from apps.myread import models as mdmyread
from apps.reader import models as mdreader
from apps.book import models as mdbook


# Create your views here.
def home_page(request):
    # View can return valid formats like html, xml, json etc
    total_readers_cnt = mdreader.Reader.objects.distinct('username').count()
    engaged_reader_cnt = mdmyread.MyRead.objects.distinct('reader_username').count()
    book_per_cat_cnt = mdbook.Book.objects.values('category').annotate(cnt=Count('*'))

    context = {
        'total_readers_cnt': total_readers_cnt,
        'engaged_reader_cnt': engaged_reader_cnt,
        'book_per_cat_cnt': book_per_cat_cnt
    }

    # Return the response
    return render(request, 'home_page.html', context)

class HomePage(TemplateView):
    # Specify the templates to display
    template_name = 'home_page.html'
