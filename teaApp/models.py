from django.db import models

# Create your models here.

class Order(models.Model):

    name = models.CharField(null = False, max_length=200)
    order = models.TextField(null = False, max_length= 200)
    extras = models.TextField(null = True, max_length=200)
    sugar = models.IntegerField(null = True)

    def __str__(self):
        return self.name

class Drink(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Names(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  
     
class Extras(models.Model):
    extra = models.CharField(max_length=100)

    def __str__(self):
        return self.extra