from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=100)
    email = models.EmailField(unique=True,max_length=254)
    city = models.CharField(max_length=100,default='Unkown')

    def __str__(self):
        return self.name