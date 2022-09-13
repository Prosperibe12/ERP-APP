from django.db import models 

# Create your custom managers here
"""
All custom managers for the employee section of this application will be registered here
"""

# custom QuerySet for Department Model
class EmployeeQuerySet(models.QuerySet):
    
    # get department by id
    def get_dept(self, id):
        if id is None or id == "":
            self.none()
        return self.get(id=id)
    
    # get job position by id
    def get_job(self, id):
        if id is None or id == "":
            self.none()
        return self.get(id=id)
    
    # get employee by id
    def get_employee(self,id):
        if id is None or id == "":
            self.none()
        return self.get(id=id)
    
    # get contract details by id
    def get_contract(self,id):
        if id is None or id == "":
            self.none()
        return self.get(id=id)
    
    # get employee contract
    def employee_contract(self,employee):
        if employee is None or employee == "":
            self.none()
        return self.filter(employee=employee)
    
    # get employee by dept
    def employee_dept(self,dept):
        if dept is None or dept == "":
            self.none()
        return self.filter(dept=dept)
    
# custom manager for Department Model
class DepartmentManager(models.Manager):
    
    def get_queryset(self):
        return EmployeeQuerySet(self.model, using=self._db)
    
    def get_dept(self, id):
        return self.get_queryset().get_dept(id)
    
# custom manager for Job Position model 
class JobPositionManager(models.Manager):
    
    def get_queryset(self):
        return EmployeeQuerySet(self.model, using=self._db)
    
    def get_job(self, id):
        return self.get_queryset().get_job(id)
    
# custom queryset for Employee model
class EmployeeManager(models.Manager):
    
    def get_queryset(self):
        return EmployeeQuerySet(self.model, using=self._db)
    
    # get employee by id
    def get_employee(self,id):
        return self.get_queryset().get_employee(id)
    
    # get employee by dept
    def employee_dept(self,dept):
        return self.get_queryset().employee_dept(dept)

# custom queryset for Employee Contract model   
class EmployeeContractManager(models.Manager):
    
    def get_queryset(self):
        return EmployeeQuerySet(self.model, using=self._db)
    
    def get_contract(self,id):
        return self.get_queryset().get_contract(id)
    
    def employee_contract(self,employee):
        return self.get_queryset().employee_contract(employee)
