from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField('title', max_length=100)
    stock = models.IntegerField('stock', default=0)
    
    def __str__(self):
        return self.title
   