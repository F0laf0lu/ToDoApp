from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)   
    updated_on = models.DateField(auto_now=True)