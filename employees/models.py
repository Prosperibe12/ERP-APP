from datetime import datetime
from distutils.command.upload import upload
import secrets
import random, string
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from dateutil.relativedelta import relativedelta
from datetime import date
from django.db import models
from django.contrib.auth.models import User 
from .managers import *

# Create your models here.
"""
All models and custom model manager for the employee section of this application will be registered here
"""
# models for job position
class JobPosition(models.Model):
    name = models.CharField(max_length=150)
    job_description = models.TextField(max_length=250)
    no_employee = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    objects = JobPositionManager()
    
    def __str__(self):
        return f'{self.name}'

# Department model 
class Department(models.Model):
    name = models.CharField(max_length=50)
    manager = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    objects = DepartmentManager()
    
    def __str__(self):
        return f'{self.name}'
            
class Employee(models.Model):
    
    ACCESS_LEVEL = (
        ('General', 'General'),
        ('Staff', 'Staff'),
        ('Manager', 'Manager'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_pix = models.ImageField(upload_to="employee_pix", blank=True, null=True)
    full_name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField()
    mobile = models.CharField(blank=False, null=False, max_length=50)
    gender = models.CharField(choices=GENDER, null=True, blank=True, max_length=50)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE, null=True, blank=True)
    dept_coach = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='manager')
    level = models.CharField(max_length=50, choices=ACCESS_LEVEL, null=False, blank=False)
    badge_id = models.CharField(max_length=50, blank=True, null=True)
    next_appraisal = models.DateField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    objects = EmployeeManager()     
    
    def __str__(self):
        return f'{self.full_name}'
    
    # create next appraisal date
    # def save(self, *args, **kwargs):
    #     today = datetime.now()
    #     self.next_appraisal = today + relativedelta(months=+6)
    #     return super().save( *args, **kwargs)
    
    # auto generated badge id
    def save(self, *args, **kwargs):
        while not self.badge_id:
            code = "REL"
            i_badge_id = random.randint(1, 1000000)
            f_badge_id = str(i_badge_id)
            badge_id = code+f_badge_id
            sm_badge_id = Employee.objects.filter(badge_id=badge_id)
            if not sm_badge_id:
                self.badge_id = badge_id
        
        today = datetime.now()
        self.next_appraisal = today + relativedelta(months=+6)
        return super().save(*args, **kwargs)
       
class EmployeeContract(models.Model):
    
    SALARY_STRUCTURE = (
        ('Employee', 'Employee'),
        ('Contract', 'Contract'),
    )
    
    CONTRACT_STATUS = (
        ('New', 'New'),
        ('Running', 'Running'),
        ('Expired', 'Expired'),
    )
    contract_reference = models.CharField(max_length=150, blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE, blank=True, null=True)
    acc_no = models.IntegerField(blank=True, null=True)
    bank_name = models.CharField(max_length=50)
    salary_type = models.CharField(choices=SALARY_STRUCTURE, max_length=150)
    salary_details = models.TextField(blank=True, null=True)
    start_date  = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(choices=CONTRACT_STATUS, max_length=120, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = EmployeeContractManager()
    
    def __str__(self):
        return f'{self.id}'
    
    # randomly generate a unique contract ref
    def save(self, *args, **kwargs):
        while not self.contract_reference:
            pre_name = "CRT"
            pre_ref = random.randint(1, 1000000)
            pos_ref = str(pre_ref)
            contract_reference = pre_name + pos_ref
            sm_ref = EmployeeContract.objects.filter(contract_reference=contract_reference)
            if not sm_ref:
                self.contract_reference = contract_reference
        return super().save(*args, **kwargs)

    
    


    
    
    
    
