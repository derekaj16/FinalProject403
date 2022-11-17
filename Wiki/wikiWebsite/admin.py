from django.contrib import admin
from .models import Person, Subscriber, Article, Comment, Paragraph

# Register your models here.
admin.site.register(Person)
admin.site.register(Subscriber)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Paragraph)