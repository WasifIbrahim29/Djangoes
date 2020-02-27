from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .forms import SearchForm

# Create your views here.


def index(request):
    return render(request,'first_app/index.html')

def home(request):
    return HttpResponse("Welcome to wasif page!")

def educative(request):
    return HttpResponse("Welcome to Educative page!")

def forms(request):
    form = SearchForm()
    return render(request,'first_app/forms.html', {'form': form})