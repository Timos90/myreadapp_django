from django.urls import path
from . import views

app_name = 'book-urls'

urlpatterns = [
    path('book/<isbn>', views.book_detail, name='book-detail'),
    # in most cases post hhtp method may not work without ending slash(/)
    path('book/post/', views.book_post, name='book-post'),
]
