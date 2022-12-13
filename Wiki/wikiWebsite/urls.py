from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPageView, name='index'),
    path('about', aboutPageView, name='about'),
    path('subscribe', subscribeView, name='subscribe'),
    path('article/<int:id>', articlePageView, name='article'),
    path('my_articles', myArticlesPageView, name='my_articles'),
    path('articles', allArticlesPageView, name='all_articles'),
    path('login', loginPageView, name='login'),
    path('logout', logoutView, name='logout'),
    path('signup', signUpPageView, name='signup'),
    path('create_account', createAccountView, name='create_account'),
    path('reset', resetPasswordView, name='reset'),
    path('account', accountSettingsPageView, name='account'),
    path('create', createArticlePageView, name='create'),
    path('update_article', updateArticleView, name='update_article'),
    path('delete_article/<int:id>', deleteArticle, name='delete_article'),
    path('comment/<int:user_id>/<int:article_id>', commentOnArticle, name='comment'), 
    path('delete_comment/<int:article_id>/<int:comment_id>', deleteComment, name='delete_comment'),
    path('change-pass', changePasswordPageView, name='change_pass'),
    path('account', accountSettingsPageView, name='account'),
    path('search', searchArticle, name='search')
]