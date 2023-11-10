from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def rohit (request):
    return render (request,'rohit.html')

def polly (request):
    return HttpResponse ('<h1> polly is one of the best finisher in mi </h1>')