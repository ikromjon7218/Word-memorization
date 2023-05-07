from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=32)      # full name
    about = models.CharField(max_length=1000)   # about the book
    def __str__(self):
        return self.name

class Word(models.Model):
    name = models.CharField(max_length=35)                      # full name
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    unit = models.PositiveSmallIntegerField()         # Unit number
    def __str__(self):
        return self.name

class Soz(models.Model):
    name = models.CharField(max_length=35)                      # full name
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

