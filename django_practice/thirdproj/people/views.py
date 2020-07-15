from django.shortcuts import render
from .models import person
# Create your views here.

def home(request) :
    persons = person.objects
    return render(request,'home.html',{'persons':persons})
