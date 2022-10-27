from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def indexPageView(request) :
    return HttpResponse('WE IS SMART')

def articlePageView(request) : # add params
    return HttpResponse('article page view')

def aboutPageView(request) :
    return HttpResponse('about page view')

def contactPageView(request) :
    return HttpResponse('contact page view')

def searchPageView(request) :
    return HttpResponse('search page view')

def subscribePageView(request) :
    return HttpResponse('subscribe page view')