from django.shortcuts import render
from django.http import HttpResponse
from . import crawling

# Create your views here.

def getImage(request):
    crawling.urllib_request_loop()
    return HttpResponse(200)