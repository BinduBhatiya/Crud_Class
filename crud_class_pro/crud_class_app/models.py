from django.db import models

# Create your models here.
class Student(models.Model):
    first_nm = models.CharField(max_length=15)
    last_nm = models.CharField(max_length=15)
    mail = models.EmailField()
    city = models.CharField(max_length=15)

def __str__(self):
    return self.first_nm
    
