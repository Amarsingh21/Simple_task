from django.db import models

# Create your models here.
class Student(models.Model):
    # id=models.IntegerField()
    name=models.CharField(max_length=100)
    school=models.CharField(max_length=100)
    address=models.CharField(max_length=150)
    rollno=models.IntegerField()
    Mobileno=models.IntegerField()
    email=models.EmailField(max_length=50)
