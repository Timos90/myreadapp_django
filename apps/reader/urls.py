from django.urls import path
from . import views

app_name = 'reader-urls'
urlpatterns = [
    path('reader/login/', views.login_view, name='reader-login'), # Slash only for POST
    path('reader/profile', views.profile, name='reader-profile') # GET doesnt need a slash
]
