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
        'title': 'article',
        'articleTitle': 'How To Date',
        'paragraph': ['this is my first paragraph', 'this is my second paragraph', 'this is my third paragraph', 'fourth paragraph lets gooooooooooooo'],
        'dateCreated': 'Sep 7, 2022',
        'authorName': 'Derek Johnson'
    }
    return render(request, 'wikiWebsite/article.html', context)

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

def articlesListPageView(request) :
    context = {
        'title': 'articles_list',
        'articleTitles': ['How To Date', 'How Not to Date', 'LOL, Why Not']
    }
    return render(request, 'wikiWebsite/article_list.html', context)