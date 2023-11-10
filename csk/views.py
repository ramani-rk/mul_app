from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dhoni (request):
    return render (request,'dhoni.html')

def jaddu (request):
    return HttpResponse ('<h1>  jaddu is the best all rounder </h1>')