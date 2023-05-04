from django.db import models
# from mongoengine import Document,fields

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
