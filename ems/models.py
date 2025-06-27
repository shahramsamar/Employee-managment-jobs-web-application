from django.db import models


class Employee(models.Model):
    GENDER_CHOICES = [("M",'Male'),
                      ('F',"Female"),
                      ("O","Other")]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=13,blank=True)
    address = models.TextField(null=True,blank=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True)
    Birthday = models.DateField()
    joining_date = models.DateField()
    jobs = models.ManyToManyField("Job",blank=True)

class Job(models.Model):
    name = models.CharField(max_length=255)  
      
    def __str__(self) -> str:
         return self.name