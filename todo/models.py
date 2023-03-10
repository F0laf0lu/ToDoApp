from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)   
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.content