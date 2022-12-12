from django.db import models
from datetime import datetime


class Subscriber(models.Model) :
    dateSubscribed = models.DateField(default=datetime.today)

    def __str__(self) :
        return self.dateSubscribed

    class Meta :
        db_table = 'subscriber'

class Author(models.Model) :
    dateBecameAuthor = models.DateField(default=datetime.today)
    about = models.TextField(max_length=1000, blank=True)

    def __str__(self) :
        return self.dateBecameAuthor

    class Meta :
        db_table = 'author'

class Person(models.Model) :
    STATUS = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('E', 'Engaged'),
        ('R', 'In a relationship'),
        ('O', 'Other')
    )
    firstname = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=500)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE, null=True, blank=True, db_column='subscriber_id')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, db_column='author_id')
    status = models.CharField(max_length=20, choices=STATUS, null=True, blank=True)

    def __str__(self) :
        return self.firstname + self.lastname

    class Meta :
        db_table = 'person'

class Article(models.Model) :
    header = models.CharField(max_length=200)
    subheader = models.CharField(max_length=300)
    content = models.TextField()
    date_created = models.DateTimeField(default=datetime.today())
    date_last_updated = models.DateTimeField(default=datetime.today())
    author = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, db_column='author_id')

    def __str__(self) :
        return self.header

    class Meta :
        db_table = 'article'

class Comment(models.Model) :
    commentText = models.TextField(blank=False)
    personID = models.ForeignKey(Person, on_delete=models.CASCADE)
    articleID = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta :
        db_table = 'comment'
