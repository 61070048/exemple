from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
       return self.name 

class Choice(models.Model):
    name = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
       return self.name  