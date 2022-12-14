from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from hashlib import sha256
from datetime import date
from datetime import datetime
import re


salt = '2%5!#b2wr3SIs601c616f509c7b2374ffa12ef51d3d0bcfa511c2e7e8d4e4a5cbd678b7cf5e!#$12ef51d3d0bcfa511c$@1saTeRwq093&2jsfld'

status = (
    ('S', 'Single'),
    ('R', 'In a relationship'),
    ('E', 'Engaged'),
    ('M', 'Married'),
    ('O', 'Other')
)

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

def indexPageView(request) :
    logged_in, user = loggedIn(request)

    context = {
        'logged_in' : logged_in,
        'user' : user,
        'title' : 'Get Hitched'  
    }
    return render(request, 'wikiWebsite/index.html', context)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    VIEWS RELATED TO USER ACCOUNT    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

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

def signUpPageView(request, subscriber_email=None) :
    logged_in, user = loggedIn(request)
    if logged_in :
        return indexPageView(request)
    else :
        email_list = []
        username_list = []

        # Filling lists for validity checking
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
            'title' : 'Sign up',
            'subscriber_email' : subscriber_email
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
        password = request.POST['password']
        new_user.password = sha256((password + salt[0:(len(password) + len(username))]).encode('utf-8')).hexdigest()
        new_user.status = request.POST['status']
        new_user.about = request.POST.get('author-about')
        
        # Check if person is already a subscriber and link their 
        # subscriber email to their account
        if (request.POST['subscribe'] == 'y') :
            
            subscriber = Subscriber.objects.filter(email=request.POST['email'])

            if len(subscriber) > 0 :
                new_user.subscriber = subscriber[0]
            else :
                new_subscriber = Subscriber()
                new_subscriber.dateSubscribed = date.today()
                new_subscriber.email = request.POST['email']
                new_subscriber.save()
                new_user.subscriber = new_subscriber

        new_user.save()

        request.session['userid'] = new_user.id

    return redirect(indexPageView)

def resetPasswordView(request) :
    # if request.method == 'POST' :

    return render(request, 'wikiWebsite/reset_pass.html')

def changePasswordPageView(request) :
    logged_in, user = loggedIn(request)

    if request.method == 'POST' :
        password = request.POST['password']
        user.password = sha256((password + salt[0:(len(password) + len(user.username))]).encode('utf-8')).hexdigest()
        user.save()

        request.method = 'GET'

        return accountSettingsPageView(request, pass_changed=True)
    
    else :
        context = {
            'logged_in' : logged_in,
            'user' : user
        }

        return render(request, 'wikiWebsite/change_pass.html', context)

def accountSettingsPageView(request, pass_changed=False) :
    logged_in, user = loggedIn(request)
    email_list = []
    username_list = []

    emails = Person.objects.values('email')
    for email in emails :
        email_list.append(email['email'])
    usernames = Person.objects.values('username')
    for username in usernames :
        username_list.append(username['username'])

    if request.method == 'POST' :
        user.firstname = request.POST['firstname'].title()
        user.lastname = request.POST['lastname'].title()
        user.email = request.POST['email']
        user.username = request.POST['username']
        user.status = request.POST['status']
        user.save()

        return redirect(accountSettingsPageView)

    context = {
        'logged_in' : logged_in,
        'user' : user,
        'emails' : email_list,
        'usernames' : username_list,
        'options': status,
        'pass_changed' : pass_changed,
        'statuses' : status,
        'user_email' : user.email,
        'user_username' : user.username
    }
    return render(request, 'wikiWebsite/acc_settings.html', context)

def addBio(request) :
    logged_in, user = loggedIn(request)
    if request.method == 'POST' :
        user.about = request.POST['about']
        print(request.POST['about'])
        user.save()
    
    return redirect(accountSettingsPageView)

def deleteAccount(request, user_id) :
    user = Person.objects.get(id=user_id)
    user_articles = Article.objects.select_related('author').filter(author_id=user.id)

    if len(user_articles) > 0:
        for article in user_articles :
            article.delete()

    user.delete()

    request.session['userid'] = None
    return redirect(indexPageView)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    VIEWS RELATED TO ARTICLES    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def allArticlesPageView(request) : # add params
    logged_in, user = loggedIn(request)
    all_articles = Article.objects.all()
    featured_articles = []

    for i in range(0,4) :
        featured_articles.append(all_articles[i])

    context = {
        'logged_in' : logged_in,
        'user' : user,
        'title': 'Articles',
        'articles': all_articles,
        'featured_articles': featured_articles
    }
    return render(request, 'wikiWebsite/all_articles.html', context)

def articlePageView(request, id) : # add params
    logged_in, user = loggedIn(request)
    article = Article.objects.select_related('author').get(id=id)
    comments = Comment.objects.select_related('personID').filter(articleID=id)

    context = {
        'logged_in' : logged_in,
        'user' : user,
        'title': article.header,
        'article' : article,
        'comments' : comments, 
        'content_no_break' : article.content.replace('<br>', '')
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

def returnSpace(content, curr_index, next_space=True) :
    while content[curr_index] != ' ' :
        # If we are looking for a space AFTER the word
        if next_space :
            curr_index += 1
        # If we are look for a space BEFORE the word
        else :
            curr_index -= 1
    return curr_index

def highlight(str, search, start) :
    end = start + len(search)
    content = ''
    
    if start >= 100 :
        content += '...' + str[returnSpace(str, (start - 100), False):start] 
    else :
        content += str[0:start] 
    
    content += '<span class="highlight">' + str[start:end] + '</span>' 
    
    if (len(str) - end) >= 100 :
        content += str[end:returnSpace(str, (end+100), True)] + ' ...'
    else :
        content += str[end:]
        
    
    return content

def searchArticle(request) :
    logged_in, user = loggedIn(request)
    
    if (request.method == 'GET') :
        title = ''
        content = ''
        results = []
        query = request.GET['search'].lower()
        articles = Article.objects.all()
    
        if len(articles) > 0 :
            for article in articles :
                if query in article.header.lower() :
                    title = highlight(article.header, query, re.search(query, article.header, re.IGNORECASE).span()[0])
                    if query in article.content.lower() :
                        content = highlight(article.content, query, re.search(query, article.content, re.IGNORECASE).span()[0])
                        results.append([title, content, article.id])
                    else :
                        content = article.content[0:200] + '...'
                        results.append([title, content, article.id])

                elif query in article.content.lower() :
                    title = article.header
                    content = highlight(article.content, query, re.search(query, article.content, re.IGNORECASE).span()[0])
                    results.append([title, content, article.id])

        context = {
            'query' : query,
            'logged_in' : logged_in,
            'user' : user,
            'title' : 'Search',
            'results' : results
        }
        return render(request, 'wikiWebsite/search.html', context)

def subscribePageView(request) :
    logged_in, user = loggedIn(request)
    subscribed = False

    if request.method == 'GET' :
        new_subscriber = Subscriber()
        new_subscriber.email = user.email
        new_subscriber.dateSubscribed = datetime.today()
        new_subscriber.save()

        user.subscriber = new_subscriber
        user.save()
    
        return redirect(accountSettingsPageView)


    if request.method == 'POST' :
        subscribed = True
        new_subscriber = Subscriber()
        new_subscriber.email = request.POST['email']
        new_subscriber.dateSubscribed = datetime.today()
        new_subscriber.save()

    context = {
        'subscribed' : subscribed,
        'logged_in' : logged_in,
        'user' : user
    }

    return render(request, 'wikiWebsite/subscribe.html', context)

def myArticlesPageView(request) :
    logged_in, user = loggedIn(request)
    articles = Article.objects.filter(author_id=user.id)

    context = {
        'logged_in' : logged_in,
        'user' : user,
        'articles' : articles,
        'title': 'Article List',
        'articleTitles': ['How To Date', 'How Not to Date', 'LOL, Why Not']
    }
    
    return render(request, 'wikiWebsite/my_articles.html', context)

def parseNewLine(str) :
    content = ''

    for character in str :
        if character == '\n' :
            content += '<br>'
        else :
            content += character

    return content

def createArticlePageView(request) :
    logged_in, user = loggedIn(request)
    all_users = Person.objects.all()

    if request.method == 'POST' :
        new_article = Article()
        new_article.header = request.POST['heading']
        new_article.subheader = request.POST['subheading']
        new_article.content = parseNewLine(request.POST['content'])
        new_article.date_created = datetime.today()
        new_article.date_last_updated = datetime.today()
        new_article.author = user
        new_article.save()

        return redirect(myArticlesPageView)

    else :
        context = {
            'logged_in' : logged_in,
            'user' : user,
            'all_users' : all_users,
            'title' : 'Create Article'
        }
        return render(request, 'wikiWebsite/create_article.html', context)

# a view function that creates a new article using the form inputs of the create_article.html page and saves it to the database
def updateArticleView(request) :
    
    if request.method == 'POST' :
        article_id = request.POST['article_id']
        article = Article.objects.get(id=article_id)
        article.header = request.POST['header']
        article.subheader = request.POST['subheader']
        article.content = parseNewLine(request.POST['content'])
        article.save()

        return redirect('/article/' + str(article_id))

def deleteArticle(request, id) :
    article = Article.objects.get(id=id)
    article.delete()

    return redirect(myArticlesPageView)

def commentOnArticle(request, article_id, user_id ) :
    if request.method == 'POST' :
        new_comment = Comment()

        new_comment.articleID = Article.objects.get(id=article_id)
        new_comment.commentText = parseNewLine(request.POST['comment'])
        new_comment.personID = Person.objects.get(id=user_id)
        new_comment.save()

        request.method == 'GET'
    
    return redirect('/article/' + str(article_id))

def deleteComment(request, article_id, comment_id) :
    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return redirect('/article/' + str(article_id))