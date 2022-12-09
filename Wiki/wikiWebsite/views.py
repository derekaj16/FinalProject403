from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from hashlib import sha256
from datetime import date


salt = '2%5!#b2wr3SIs601c616f509c7b2374ffa12ef51d3d0bcfa511c2e7e8d4e4a5cbd678b7cf5e!#$12ef51d3d0bcfa511c$@1saTeRwq093&2jsfld'

def loggedIn(request) :
    logged_in = False
    if 'userid' in request.session :
        if not request.session['userid'] == None :
            user = Person.objects.get(id=request.session['userid'])
            logged_in = True
        else :
            user = None
    else :
        user = None

    return logged_in, user

# Create your views here.

def indexPageView(request) :
    logged_in, user = loggedIn(request)

    context = {
        'logged_in' : logged_in,
        'user' : user,
        'title' : 'Get Hitched'  
    }
    return render(request, 'wikiWebsite/index.html', context)

def loginPageView(request) :
    error = False
    logged_in, user = loggedIn(request)

    print('login view ' + request.method)

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        usernames = Person.objects.values_list('username')

        for name in usernames :
            print(name[0])
        if len(usernames) > 0 :
            for name in usernames :
                if username == name[0] :
                    user = Person.objects.get(username=username)
                    hash_password = sha256((password + salt[0:(len(password) + len(username))]).encode('utf-8')).hexdigest()

                    if hash_password == user.password :
                        request.session['userid'] = user.id
                        return redirect(indexPageView)

                    else :
                        error = True
                else :
                    error = True
            else :
                error = True

    context = {
        'error': error,
        'logged_in' : logged_in,
        'user' : user,
        'title' : 'Log in'
    }

    return render(request, 'wikiWebsite/login.html', context)

def logoutView(request) :
    request.session['userid'] = None
    return redirect(indexPageView)

def signUpPageView(request) :
    logged_in, user = loggedIn(request)

    status = (
        ('S', 'Single'),
        ('R', 'In a relationship'),
        ('E', 'Engaged'),
        ('M', 'Married'),
        ('O', 'Other')
    )

    
    email_list = []
    username_list = []

    emails = Person.objects.values('email')
    for email in emails :
        email_list.append(email['email'])
    usernames = Person.objects.values('username')
    for username in usernames :
        username_list.append(username['username'])
        

    context = {
        'usernames' : username_list,
        'emails' : email_list,
        'options' : status,
        'logged_in' : logged_in,
        'user' : user,
        'title' : 'Sign up'
    }
    return render(request, 'wikiWebsite/signup.html', context)

def createAccountView(request) :

    if request.method == 'POST' :
        new_user = Person()
        new_user.firstname = request.POST['firstname'].title()
        new_user.lastname = request.POST['lastname'].title()
        new_user.email = request.POST['email']
        username = request.POST['username']
        new_user.username = username
        #Hashing the password baby (and adding salt for some taste mmmm)
        password = request.POST['password']
        new_user.password = sha256((password + salt[0:(len(password) + len(username))]).encode('utf-8')).hexdigest()
        new_user.status = request.POST['status']
        
        if (request.POST['subscribe']) :
            new_subscriber = Subscriber()
            new_subscriber.dateSubscribed = date.today()
            new_subscriber.save()

            new_user.subscriber = new_subscriber
        
        if (request.POST.get('author')) :
            new_author = Author()
            new_author.dateBecameAuthor = date.today()
            new_author.about = request.POST.get('author-about')
            new_author.save()

            new_user.author = new_author

        new_user.save()

        request.session['userid'] = new_user.id

    return redirect(indexPageView)

def articlePageView(request) : # add params
    logged_in, user = loggedIn(request)

    context = {
        'logged_in' : logged_in,
        'user' : user,

        'title': 'Articles',
        'articleTitle': 'How To Date',
        'paragraph': ['this is my first paragraph', 'this is my second paragraph', 'this is my third paragraph', 'fourth paragraph lets gooooooooooooo'],
        'dateCreated': 'Sep 7, 2022',
        'authorName': 'Derek Johnson'
    }
    return render(request, 'wikiWebsite/article.html', context)

def aboutPageView(request) :
    logged_in, user = loggedIn(request)

    person_data = Person.objects.all()
    context = {
        'title': 'About Us',
        'authors': person_data,
        'logged_in' : logged_in,
        'user' : user,
    }
    return render(request, 'wikiWebsite/about.html', context)

def contactPageView(request) :
    logged_in, user = loggedIn(request)

    context = {
        'logged_in' : logged_in,
        'user' : user,
        'title' : 'Contact Us'
    }
    return render(request, 'wikiWebsite/index.html', context)

def searchPageView(request) :
    logged_in, user = loggedIn(request)

    context = {
        'logged_in' : logged_in,
        'user' : user,
        'title' : 'Search'
    }
    return render(request, 'wikiWebsite/index.html', context)

def subscribePageView(request) :
    logged_in, user = loggedIn(request)

    context = {
        'logged_in' : logged_in,
        'user' : user,
        'title' : 'Subscribe'
    }
    return render(request, 'wikiWebsite/index.html', context)

def articlesListPageView(request) :
    logged_in, user = loggedIn(request)

    context = {
        'logged_in' : logged_in,
        'user' : user,

        'title': 'Article List',
        'articleTitles': ['How To Date', 'How Not to Date', 'LOL, Why Not']
    }
    return render(request, 'wikiWebsite/article_list.html', context)