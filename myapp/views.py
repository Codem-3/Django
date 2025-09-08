from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>Hello World! 🐍</h1>
    <p>This is a test of the home page.</p>
    <a href="/about/">About</a>
    <a href="/contact/">Contact</a>
    """)