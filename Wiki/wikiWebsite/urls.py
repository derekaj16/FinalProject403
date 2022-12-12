from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPageView, name='index'),
    path('about', aboutPageView, name='about'),
    path('contact', contactPageView, name='contact'),
    path('subscribe', subscribeView, name='subscribe'),
    path('articles', articlePageView, name='articles'),
    path('my_articles', myArticlesPageView, name='my_articles'),
    path('all_articles', allArticlesPageView, name='all_articles'),
    path('login', loginPageView, name='login'),
    path('logout', logoutView, name='logout'),
    path('signup', signUpPageView, name='signup'),
    path('create_account', createAccountView, name='create_account'),
    path('reset', resetPasswordView, name='reset'),
    path('account', accountSettingsPageView, name='account'),
    path('create', createArticlePageView, name='create'),
    path('update_article', updateArticleView, name='update_article'),
    # path('delete_article', deleteArticleView, name='delete_article'),
    path('change-pass', changePasswordPageView, name='change_pass'),
    path('account', accountSettingsPageView, name='account'),
    path('search', searchArticle, name='search')
]