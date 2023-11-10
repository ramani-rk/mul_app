from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def virat (request):
    return render (request,'virat.html')

def faf (request):
    return HttpResponse ('<h1> faf is the former player of the CSK...</h1> <h1>Now faf is the captain of RCB </h1>')