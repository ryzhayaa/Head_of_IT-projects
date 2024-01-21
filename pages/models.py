from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
# Create your models here.
from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=200)
    key_skills = models.TextField(null=True, blank=True)
    salary_from = models.FloatField(null=True, blank=True)
    salary_to = models.FloatField(null=True, blank=True)
    salary_currency = models.CharField(max_length=50, null=True, blank=True)
    area_name = models.CharField(max_length=200, null=True, blank=True)
    published_at = models.DateTimeField()
