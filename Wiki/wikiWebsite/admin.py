from django.contrib import admin
from .models import Author, Subscriber, Article, Comment, Person

# # Register your models here.
admin.site.register(Author)
admin.site.register(Subscriber)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Person)