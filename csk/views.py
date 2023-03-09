from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('<h1> ms dhoni is a best capten</h1>')
def jadeja(request):
    return HttpResponse('all rounder')   