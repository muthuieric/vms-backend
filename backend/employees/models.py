from django.db import models

 # Create your models here. 
class Employee(models.Model):
    Name = models.CharField(max_length=255)
    Job_title = models.CharField(max_length=255)
    Id_number = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField()


    def __str__(self):
        return self.Name
