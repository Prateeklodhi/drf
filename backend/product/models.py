from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=15,default=9.9)