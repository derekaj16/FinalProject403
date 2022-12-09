from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPageView, name='index'),
    path('about', aboutPageView, name='about'),
    path('contact', contactPageView, name='contact'),
    path('subscribe', subscribePageView, name='subscribe'),
    path('search', searchPageView, name='search'),
    path('articles', articlePageView, name='articles'),
    path('my-articles', myArticlesPageView, name='my_articles'),
    path('login', loginPageView, name='login'),
    path('logout', logoutView, name='logout'),
    path('signup', signUpPageView, name='signup'),
    path('create_account', createAccountView, name='create_account'),
    path('reset', resetPasswordView, name='reset'),
    path('account', accountSettingsPageView, name='account')
]