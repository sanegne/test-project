from django.db import models


# Create your models here.
class GenreType(models.TextChoices):    
    Contemporary = 'Contemporary'    
    Detective = 'Detective'
    Dystopian = 'Dystopian'
    Fantasy = 'Fantasy'
    Horror = 'Horror'    
    Mystery = 'Mystery'
    Romance = 'Romance'
    Thriller = 'Thriller'


class Book(models.Model):
    author = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    synopsis = models.TextField()
    genere = models.CharField(max_length=50, choices=GenreType.choices, default=GenreType.Contemporary)
    released = models.DateField()
    price = models.IntegerField(default=0) # 100 cents = 1$
