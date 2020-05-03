from django.db import models

# Create your models here.
class Choice(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
       return self.name

class Question(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
       return self.name   