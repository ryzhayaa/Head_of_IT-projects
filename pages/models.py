from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
# Create your models here.
