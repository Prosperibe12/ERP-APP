from tkinter import Widget
from django import forms 
from .models import * 

# Create your forms here.
"""
All forms for the employee section of this application will be registered here
"""

class JobPositionForm(forms.ModelForm):
    
    name = forms.CharField(label=('Job Position'), widget=forms.TextInput(attrs={'class':'form-control'}))
    job_description = forms.CharField(label=('Job Decription'), widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))
    no_employee = forms.CharField(label=('Expected No of Employee'), widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = JobPosition
        fields = ['name', 'job_description', 'no_employee']
        
    # validate field
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == "":
            raise forms.ValidationError("Name Field Cannot be Blank")

        for names in JobPosition.objects.all():
            if names.name == name:
                raise forms.ValidationError(f'{name} Already Exist.')
        return name
        
class DepartmentForm(forms.ModelForm):
    
    name = forms.CharField(label=('Department Name'), widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Department
        fields = ['name','manager']
        widgets = {
            'manager': forms.Select(attrs={'class':'form-select'})
        }
    
    # perform validations  
    # check if a depf already exist
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == "":
            raise forms.ValidationError("Name Field Cannot be Blank")

        for names in Department.objects.all():
            if names.name == name:
                raise forms.ValidationError(f'{name} Already Exist.')
        return name
    
class EmployeeContractForm(forms.ModelForm):
    
    acc_no = forms.CharField(label=('Account Number'), widget=forms.NumberInput(attrs={'class':'form-control'}))
    bank_name = forms.CharField(label=('Bank Name'), widget=forms.TextInput(attrs={'class':'form-control'}))
    salary_details = forms.CharField(label=('Salary Details'), widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))
    start_date = forms.CharField(label=('Start Date'), widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    end_date = forms.CharField(label=('Start Date'), widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    
    class Meta:
        model = EmployeeContract
        exclude = ['contract_reference','created_at']
        widgets = {
            'employee': forms.Select(attrs={'class':'form-select'}),
            'department': forms.Select(attrs={'class':'form-select'}),
            'job_position': forms.Select(attrs={'class':'form-select'}),
            'salary_type': forms.Select(attrs={'class':'form-select'}),
            'status': forms.Select(attrs={'class':'form-select'})
        }
        
class EmployeeForm(forms.ModelForm):
    
    full_name = forms.CharField(label=('Full Name'), widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label=('Email'), widget=forms.EmailInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(label=('Phone No'), widget=forms.TextInput(attrs={'class':'form-control'}))
        
    class Meta:
        model = Employee
        exclude = ['date_created','next_appraisal']
        widgets = {
            'user':forms.Select(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'dept': forms.Select(attrs={'class':'form-select'}),
            'job_position': forms.Select(attrs={'class':'form-select'}),
            'dept_coach': forms.Select(attrs={'class':'form-select'}),
            'level': forms.Select(attrs={'class':'form-select'}),
        }
    
    # validate email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email == "":
            raise forms.ValidationError("This Field Cannot be Empty")
        
        for emails in Employee.objects.all():
            if emails.email == email:
                raise forms.ValidationError(f'{email} already Exist.')
        return email 
        
# update forms
class EmployeeUpdateForm(forms.ModelForm):
    
    full_name = forms.CharField(label=('Full Name'), widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label=('Email'), widget=forms.EmailInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(label=('Phone No'), widget=forms.TextInput(attrs={'class':'form-control'}))
    next_appraisal = forms.CharField(label=('Next Appraisal'), widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
        
    class Meta:
        model = Employee
        exclude = ['user','gender','profile_pix','badge_id','date_created']
        widgets = {
            'gender': forms.Select(attrs={'class':'form-select'}),
            'dept': forms.Select(attrs={'class':'form-select'}),
            'job_position': forms.Select(attrs={'class':'form-select'}),
            'dept_coach': forms.Select(attrs={'class':'form-select'}),
            'level': forms.Select(attrs={'class':'form-select'})
        }

class ContractUpdateForm(forms.ModelForm):
    
    acc_no = forms.CharField(label=('Account No'), widget=forms.TextInput(attrs={'class':'form-control'}))
    bank_name = forms.CharField(label=('Account No'), widget=forms.TextInput(attrs={'class':'form-control'}))
    salary_details = forms.CharField(label=('Salary Details'), widget=forms.Textarea(attrs={'class':'form-control','rows':'2'}))
    end_date = forms.CharField(label=('Contract End Date'), widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    
    class Meta:
        model = EmployeeContract
        exclude = ['contract_reference','department','job_position','start_date','created_at']
        widgets = {
            'employee': forms.Select(attrs={'class':'form-select'}),
            'salary_type': forms.Select(attrs={'class':'form-select'}),
            'status': forms.Select(attrs={'class':'form-select'})
        }