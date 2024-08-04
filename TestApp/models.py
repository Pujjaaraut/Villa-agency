from django.db import models

# Create your models here.
class Contact(models.Model):
    Fullname = models.CharField(max_length=100)
    Email = models.EmailField()
    Sub = models.CharField(max_length=255)
    message = models.TextField()
    
    def __str__(self):
        return self.Fullname
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    def str(self):
        return self.name;

class Signup(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    def str(self):
        return self.username;