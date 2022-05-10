from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    desc = models.TextField()

class Contact(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    query = models.TextField()
