from django.db import models

# Create your models here. 

class Employee(models.Model):
    employee_id = models.CharField(max_length=500, null=False, unique=True)  
    employee_photo = models.CharField(max_length=500, null=True)
    first_name = models.CharField(max_length=500, null=False) 
    last_name = models.CharField(max_length=500, null=False)
    city = models.CharField(max_length=500, null=False)
    email =  models.CharField(max_length=254,null=False)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField( max_length=17, blank=True) # Validators should be a list