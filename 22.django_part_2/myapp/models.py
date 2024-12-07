from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    author = models.CharField(max_length=100, verbose_name="Author")
    publication_date = models.DateField(verbose_name="Publication Date")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    pages = models.PositiveIntegerField(verbose_name="Number of Pages")

    def __str__(self):
        return self.title