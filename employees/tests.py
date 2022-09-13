from django.test import TestCase, Client
from .models import *

# Create your tests here.
class EmployeesTestCase(TestCase):
    
    def setUp(self):
        
        # create job position
        a1 = JobPosition.objects.create(name="Accounts", job_description="Cordinate all accounts activities",
        no_employee=1)
        a2 = JobPosition.objects.create(name="HR", job_description="Cordinate all HR activities",
        no_employee=1)