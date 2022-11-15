from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def indexPageView(request) :
    context = {
        'title': 'home'
    }
    return render(request, 'wikiWebsite/index.html', context)

def articlePageView(request) : # add params
    context = {
        'title': 'article'
    }
    return render(request, 'wikiWebsite/index.html', context)

def aboutPageView(request) :
    context = {
        'title': 'about'
    }
    return render(request, 'wikiWebsite/index.html', context)

def contactPageView(request) :
    context = {
        'title': 'contact'
    }
    return render(request, 'wikiWebsite/index.html', context)

def searchPageView(request) :
    context = {
        'title': 'search'
    }
    return render(request, 'wikiWebsite/index.html', context)

def subscribePageView(request) :
    context = {
        'title': 'subscribe'
    }
    return render(request, 'wikiWebsite/index.html', context)