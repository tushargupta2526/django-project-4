from django.db import models

# Create your models here.
class Book(models.Model):
    book_no=models.IntegerField()
    book_name=models.TextField()
    author=models.CharField(max_length=100)
    price=models.FloatField()

    #we are additional metadata for model 
    class Meta:
        db_table='books'

