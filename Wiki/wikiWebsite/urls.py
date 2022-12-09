from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPageView, name='index'),
    path('about', aboutPageView, name='about'),
    path('contact', contactPageView, name='contact'),
    path('subscribe', subscribePageView, name='subscribe'),
    path('search', searchPageView, name='search'),
    path('article', articlePageView, name='article'),
    path('articles', articlesListPageView, name='article_list'),
    path('login', loginPageView, name='login'),
    path('logout', logoutView, name='logout'),
    path('signup', signUpPageView, name='signup'),
    path('create_account', createAccountView, name='create_account')
]