from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, everyone my name is shwetha, nice to meet you')
