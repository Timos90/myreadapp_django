from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Reader

# Create your views here.
def login_view(request):
    # pre-submit state
    error_message = None
    form = AuthenticationForm()



    # post-submit stage
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        # Validate the form
        if form.is_valid():
            # Extract username and password
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            reader: Reader| None = authenticate(
                username = username,
                password = password
            )
            # If authenticated, then login the reader
            if reader is not None:
                login(request, reader)
                return redirect('reader-urls:reader-profile')

        # Set an error message
        error_message = 'Sorry, something went wrong. Try again'

    context = {'form': form, 'error_message': error_message}

    return render(request, 'login.html', context)

def profile(request):
    return render(request, 'profile.html')
