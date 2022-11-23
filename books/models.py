from django.db import models


# Book object, by default no reader is specified.
class Book(models.Model):
    Name = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Description = models.TextField()
    Reader = models.CharField(default="", max_length=100)
