from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class User_data(models.Model):
    Title = models.CharField(max_length=200)
    Body = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Title} {self.Body} {self.Author}"
    
    class meta:
        db_table = "User"