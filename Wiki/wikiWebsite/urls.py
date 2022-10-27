from django.urls import path

from .views import aboutPageView, articlePageView, contactPageView, indexPageView, searchPageView, subscribePageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('about', aboutPageView, name='about'),
    path('contact', contactPageView, name='contact'),
    path('subscribe', subscribePageView, name='subscribe'),
    path('search', searchPageView, name='search'),
    path('article', articlePageView, name='article'),
]