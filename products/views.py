from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    x = 1,
    y = 2
    return HttpResponse("hello world")

def new(request):
    return HttpResponse('new function')