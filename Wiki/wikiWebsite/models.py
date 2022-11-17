from django.db import models
from datetime import datetime

class Status(models.Model) :
    status = models.CharField(max_length=30)

    def __str__(self) :
        return self.status

class Person(models.Model) :
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False, primary_key=True)
    status = models.ForeignKey(Status, blank=True, on_delete=models.CASCADE)

    def __str__(self) :
        return self.full_name

    @property
    def full_name(self) :
        return '%s %s' % (self.first_name, self.last_name)

    def save(self) :
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        super(Person, self).save()

class Subscriber(Person) :
    dateSubscribed = models.DateField(default=datetime.today)


class Author(Person) :
    dateBecameAuthor = models.DateField(default=datetime.today)

class Article(models.Model) :
    header = models.CharField(max_length=30)
    subheader = models.CharField(max_length=50)
    authors = models.ManyToManyField(Person)

    def __str__(self) :
        return self.header

class Comment(models.Model) :
    commentText = models.TextField(blank=False)
    personID = models.ForeignKey(Person, on_delete=models.CASCADE)
    articleID = models.ForeignKey(Article, on_delete=models.CASCADE)

class Paragraph(models.Model) :
    paragraphText = models.TextField(blank=False)
    articleID = models.ForeignKey(Article, on_delete=models.CASCADE)

