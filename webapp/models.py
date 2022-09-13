from django.db import models
from datetime import date

# Create your models here.
# models for handling contact messages
class Contact(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=150, null=False, blank=False)
    message = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id}'
    

# model for handling appointment
class Appointment(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(max_length=400)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id}'
    
    @property
    def check_time(self):
        if self.date and self.date < date.today():
            return True
        else:
            return False
        
  
  