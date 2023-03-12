from django.db import models

# Create your models here.

class Order(models.Model):

    name = models.CharField(max_length=200)
    order = models.TextField(null=True, blank = True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name