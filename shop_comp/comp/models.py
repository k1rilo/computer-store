from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    info = models.TextField(blank=True)
    price = models.IntegerField()
    
    
    def __str__(self) -> str:
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    key = models.ForeignKey()
    