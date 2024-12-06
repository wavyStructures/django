from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def start_page_view(request):
    return HttpResponse('<h1>Welcome to the Tech Gadgets Homepage</h1>')