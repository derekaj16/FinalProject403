from django.urls import path, include

from .views import indexPageView

urlpatterns = [
    path('', indexPageView, name='index'),
]
