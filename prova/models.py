from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    birth_country = models.CharField(max_length=50)
    
    
class Genre(models.Model):
    name = models.CharField(max_length=15)
    

class Language(models.Model):
    name = models.CharField(max_length=15)
    

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    sinopsys = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)



class Publisher(models.Model):
    name = models.CharField(max_length=15)
    
class Prueba(model.Model):
    name = models.CharField(max_length=15)
