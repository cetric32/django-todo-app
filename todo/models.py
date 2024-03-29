from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title
