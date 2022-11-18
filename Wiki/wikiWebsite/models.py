from django.db import models
from datetime import datetime

class Subscriber(models.Model) :
    dateSubscribed = models.DateField(default=datetime.today)

    def __str__(self) :
        return self.dateSubscribed

class Author(models.Model) :
    dateBecameAuthor = models.DateField(default=datetime.today)
    about = models.TextField(max_length=1000, blank=True)

    def __str__(self) :
        return self.dateBecameAuthor

class Person(models.Model) :
    STATUS = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('E', 'Engaged'),
        ('R', 'In a relationship'),
        ('O', 'Other')
    )
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False, primary_key=True)
    subscriber = models.OneToOneField(Subscriber, on_delete=models.CASCADE, null=True, blank=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, null=True, blank=True)

    def __str__(self) :
        return self.full_name

    @property
    def full_name(self) :
        return '%s %s' % (self.first_name, self.last_name)

    def save(self) :
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        super(Person, self).save()

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

