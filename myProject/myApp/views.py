from django.http import HttpResponse
from django.views import View
from .forms import UserNoteForm, RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout


def home(request):
    return render(request, 'myApp/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            # Use the save method from the form that handles password hashing
            user = form.save()  
            
            messages.success(request, "Registration successful")
            return redirect('login')  # Redirect to login page or wherever you want
    else:
        form = RegisterForm()

    return render(request, 'myApp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Get username and password from the cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)  # Log the user in
                messages.success(request, 'You are now logged in!')
                return redirect('profile')  # Redirect to the profile page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            print(form.errors)  # Log form errors for debugging
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()

    return render(request, 'myApp/login.html', {'form': form})





@login_required
def profile(request):
    user = request.user  # Get the logged-in user
    return render(request, 'myApp/profile.html', {'user': user})

@login_required
def add_note(request):
    if request.method == "POST":
        form = UserNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)  # Do not save to the database yet
            note.user = request.user  # Set the logged-in user as the note's owner
            note.save()  # Save the instance to the database
            return redirect('profile')
    else:
        form = UserNoteForm()

    return render(request, 'myApp/add_note.html', {'form': form})


@login_required
def logout_view(request):
    auth_logout(request)  # Logs out the user
    messages.success(request, "Logout Successfull")
    return redirect('login')  # Redirect to the login page


class class_view(View):
    def get(self, request):
        return HttpResponse("<h1>Welcome to class-based view page</h1>")

