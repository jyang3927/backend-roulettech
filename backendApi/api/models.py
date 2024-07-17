from django.db import models

# Create your models here.
class BookGenreChoices(models.TextChoices):
    NONFICTION = "Nonfiction"
    FICTION = "Fiction"
    
class Book(models.Model): 
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50, choices=BookGenreChoices.choices)
    date_added = models.DateTimeField(auto_add_now=True)

