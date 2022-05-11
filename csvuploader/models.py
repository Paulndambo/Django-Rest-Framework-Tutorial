from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    stadium = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    bookID = models.IntegerField()
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=500)
    average_rating = models.FloatField(default=0)
    isbn = models.CharField(max_length=200)
    isbn13 = models.CharField(max_length=200)
    language_code = models.CharField(max_length=200)
    num_pages = models.FloatField(max_length=200)
    ratings_count = models.FloatField(default=0)
    text_reviews_count = models.FloatField(default=0)
    publication_date = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)