from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from usersapp.decorators import *
from .forms import *
from .models import *
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages 
from django.http import HttpResponse
import csv


# Create your views here.
"""
All views for this users section of this app will be defined here
"""

# dept list function
# restricted page, for those only in aloowed roles
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Staff'])
def dept_index(request):
    
    department = Department.objects.all()
    data = {
        'Title': 'Departments',
        'name': 'Employees',
        'departments': department
    }
    return render(request, 'employees/department-list.html', data)

# function for department creation
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager','Staff'])
def dept_create(request):
    
    # render form to view
    form = DepartmentForm
    
    # department creation
    if request.method == 'POST':
        form = DepartmentForm(request.POST or None)
        if form.is_valid():
            department = form.cleaned_data.get('name')
            manager = form.cleaned_data.get('manager')
            # instantiate class
            dept = Department(name=department, manager=manager)
            
            # create group with dept name
            dept_group, created = Group.objects.get_or_create(name=department)
            
            # get content type for all models
            position_content_type = ContentType.objects.get_for_model(JobPosition)
            dept_content_type = ContentType.objects.get_for_model(Department)
            employee_content_type = ContentType.objects.get_for_model(Employee)
            contract_content_type = ContentType.objects.get_for_model(EmployeeContract)
            
            # query for all permissions
            position_permission = Permission.objects.filter(content_type=position_content_type)
            dept_permission = Permission.objects.filter(content_type=dept_content_type)
            employee_permission = Permission.objects.filter(content_type=employee_content_type)
            contract_permission = Permission.objects.filter(content_type=contract_content_type)
            
            # add only view permission to group from all filtered permission
            for positions in position_permission:
                if positions.codename == "view_jobposition":
                    dept_group.permissions.add(positions)
                    
            for depts in dept_permission:
                if depts.codename == "view_department":
                    dept_group.permissions.add(depts)
                    
            for employ in employee_permission:
                if employ.codename == "view_employee":
                    dept_group.permissions.add(employ)
                    
            for contracts in contract_permission:
                if contracts.codename == "view_employeecontract":
                    dept_group.permissions.add(contracts)
                    
            # save post request
            dept.save()
            messages.success(request, "Department Created Successfully")
            return redirect('employee:department-list')
            
                    
    data = {
        'Title': 'Departments',
        'name': 'Employee',
        'form': form
    }
    return render(request, 'employees/create-department.html', data)

# dept view and update function
# restricted page, for those only in aloowed roles
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Staff'])
def dept_view(request, id):
    
    dept_view = Department.objects.get_dept(id=id)
    form = DepartmentForm(instance=dept_view)
    # process post data
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=dept_view)
        if form.is_valid():
            form.save()
            messages.success(request, "Department Updated Successfully")
            return redirect('employee:department-list')
          
    data = {
        'Title': 'Departments',
        'name': 'Employees',
        'dept_view': dept_view,
        'form':form
    }
    return render(request, 'employees/department-view.html', data)

# dept update function
# restricted page, for those only in aloowed roles
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Staff'])
def dept_delete(request, id):
    
    dept_view = Department.objects.get_dept(id=id)
    #process post data
    if request.method == "POST":
        # while deleting department, delete the group
        Group.objects.filter(name=dept_view.name).delete()
        dept_view.delete()
        messages.success(request, "Department Deleted Successfully")
        return redirect('employee:department-list')
    
    data = {
        'Title': 'Departments',
        'name': 'Employees',
        'dept_view': dept_view,
    }
    return render(request, 'employees/department-delete.html', data)

# job position function
# restricted page, for those only in aloowed roles
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Staff'])
def job_position(request):
    
    jobposition = JobPosition.objects.all()
    data = {
        'name':'Employee',
        'Title':'Job Positions',
        'jobposition': jobposition
    }
    return render(request, 'employees/job-position-list.html', data)

# create job position function
# restricted page, for those only in aloowed roles
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Staff'])
def create_position(request):
    
    # form class
    form = JobPositionForm 
    # handle post data
    if request.method == 'POST':
        form = JobPositionForm(request.POST)
        if form.is_valid():
            job_name = form.cleaned_data.get('name')
            job_desc = form.cleaned_data.get('job_description')
            no_employee = form.cleaned_data.get('no_employee')
            position = JobPosition.objects.create(name=job_name, job_description=job_desc, no_employee=no_employee)
            position.save()
            messages.success(request, "Job Position Created Successfully.")
            return redirect('employee:job-list')
    
    data = {
        'name':'Employee',
        'Title':'Job Positions',
        'form': form
    }
    return render(request, 'employees/job-position-create.html', data)

# view position function
# restricted page, for those only in aloowed roles
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Staff'])
def view_position(request, id):
    
    jobposition = JobPosition.objects.get_job(id=id)
    form = JobPositionForm(instance=jobposition)
    
    # process update request
    if request.method == "POST":
        jobposition.name = request.POST.get('name')
        jobposition.job_description = request.POST.get('job_description')
        jobposition.no_employee = request.POST.get('no_employee')
        jobposition.save()
        messages.success(request, "Job Position Updated Successfully")
        return redirect('employee:job-list')
    
    data = {
        'name':'Employee',
        'Title':'Job Positions',
        'jobposition': jobposition,
        'form': form
    }
    return render(request, 'employees/job-position-view.html', data)

# delete position function
# restricted page, for those only in aloowed roles
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Staff'])
def delete_position(request, id):
    
    jobposition = JobPosition.objects.get_job(id=id)   
    # process delete request
    if request.method == "POST":
        jobposition.delete()
        messages.success(request, "Job Position Deleted Successfully")
        return redirect('employee:job-list')
    
    data = {
        'name':'Employee',
        'Title':'Job Positions',
        'jobposition': jobposition
    }
    return render(request, 'employees/job-position-delete.html', data)

# employee directory view function
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Staff'])
def employee_index(request):
    
    """
    The view for each dept will be controlled based on the User Dept except for 
    those in Admin and HR Dept with appropriate permissions.
    """
    if request.user.groups.filter(name__in=['Administration', 'HR & Development']).exists():
        employees = Employee.objects.all()
        departments = Department.objects.all()
    elif request.user.groups.filter(name='Staff').exists():
        employees = Employee.objects.filter(dept=request.user.employee.dept)
        departments = Department.objects.filter(name=request.user.employee.dept.name)
    else:
        employees = Employee.objects.filter(dept_coach=request.user)
        departments = Department.objects.filter(manager=request.user)
            
    data = {
        'name': 'Employees',
        'Title': 'Employee Directory',
        'departments': departments,
        'employees':employees,
    }
    return render(request, 'employees/employee-list.html', data)

# function to filter employees by dept
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager','Staff'])
def dept_details(request,id):
    
    employees = Employee.objects.employee_dept(dept=id)
    departments = Department.objects.get_dept(id=id)
    employee_count = employees.count()
    data = {
        'Title': 'Departments',
        'name': 'Employees',
        'departments': departments,
        'employees':employees,
        'employee_count': employee_count
    }
    return render(request, 'employees/department-details.html', data)

# employee directory create function
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Staff'])
def employee_create(request):
    
    form = EmployeeForm
    # process employee creation
    if request.method == "POST":
        form = EmployeeForm(request.POST or None, request.FILES)
        if form.is_valid():
            # add employee to group based on dept and access level
            # department = form.cleaned_data.get('dept')
            # print(department)
            # level = form.cleaned_data.get('level')
            # print(level)
            # employee = form.cleaned_data.get('user')
            # group_to_add = Group.objects.get(name=level)
            # print(group_to_add)
            # user = User.objects.filter(username=employee)
            # print("I am user:",user)
            # user.groups.add(group_to_add)
            # print("I am 3 user:",user)
            # print("Groups:", group_to_add)
            # for current_groups in group_to_add:
            #     if department == current_groups:
            #         print(True)
            #         # current_groups.user_set.add(user)
            #         user.groups.add(current_groups)
            #         print("added to:", department)
            #     if level == current_groups:
            #         print(True)
            #         # current_groups.user_set.add(user)
            #         user.groups.add(current_groups)
            #         print("added to:", level)
            # if department in group_to_add:
            #     user.groups.add(department)
            # elif level in group_to_add:
            #     user.groups.add(level)
            # else:
            #     pass
            form.save() 
            messages.success(request, "Employee Created Successfully")
            return redirect('employee:employee-list')
        else:
            messages.warning(request,"Form is not valiid")
        
    data = {
        'name': 'Employees',
        'Title': 'Employee Directory',
        'form': form
    }
    return render(request, 'employees/create-employee.html', data)

# employee list view function
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Staff'])
def employee_view(request, id):
    
    employee = Employee.objects.get_employee(id=id)
    contract = EmployeeContract.objects.employee_contract(employee=id)
    count_contract = contract.count()
    form = EmployeeUpdateForm(instance=employee)
    # process update request
    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee Updated Succesfully")
            return redirect('employee:employee-list')
    data = {
        'name': 'Employees',
        'Title': 'Employee Details',
        'employee': employee,
        'form': form,
        'contract': contract,
        'count_contract':count_contract
    }
    return render(request, 'employees/employee-view.html', data)

# employee contract directory function
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Staff'])
def contract_index(request):
    
    """
    The view for each employee contract will be controlled based on the User Dept except for 
    those in Admin and HR Dept with appropriate permissions.
    """
    if request.user.groups.filter(name__in=['Administration', 'HR & Development']).exists():
        contracts = EmployeeContract.objects.all()
    elif request.user.groups.filter(name='Staff').exists():
        contracts = EmployeeContract.objects.filter(employee=request.user.employee)
    else:
        contracts = EmployeeContract.objects.filter(department=request.user.employee.dept)
        
    data = {
        'name': 'Employees',
        'Title': 'Employee Directory',
        'contracts': contracts
    }
    return render(request, 'employees/employee-contract.html', data)

# employee contract create function
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Staff'])
def create_contract(request):
    
    form = EmployeeContractForm
    # process form
    if request.method == 'POST':
        form = EmployeeContractForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contract created Successfully.')
            return redirect('employee:list-contract')
        else:
            messages.warning(request, 'Form is not Valid')
    data = {
        'name': 'Employees',
        'Title': 'Create Contract',
        'form': form
    }
    return render(request, 'employees/create-contract.html', data)

# view contract details function
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager','Staff'])
def contract_view(request, id):
    
    contract = EmployeeContract.objects.get_contract(id=id)
    form = ContractUpdateForm(instance=contract)
    # process update form
    if request.method == 'POST':
        form = ContractUpdateForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee Contract Updated Successfully')
            return redirect('employee:list-contract')
    data = {
        'name': 'Employees',
        'Title': 'Contract Details',
        'contract': contract,
        'form': form
    }
    return render(request, 'employees/contract-view.html', data)

# function to export employee records to csv
@login_required(login_url='login')
@allowed_users(allowed_roles=['Staff','Manager'])
def employee_record(request):
    
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow(['User ID', 'FullName', 'Email', 'Mobile', 'Gender', 'Department ID', 'Job Position ID', 'Manager ID', 'Level', 'Badge ID'])
    # fetch oject from database and write to file
    for employee in Employee.objects.all().values_list('user', 'full_name', 'email', 'mobile', 'gender', 'dept', 'job_position', 'dept_coach', 'level', 'badge_id'):
        writer.writerow(employee)
        
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'
    return response

# function to export department record to csv
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager','Staff'])
def dept_record(request):
    
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow(['Department ID', 'Department Name', 'Manager ID'])
    # fetch dept table from database and write to csv
    for dept in Department.objects.all().values_list('id', 'name', 'manager'):
        writer.writerow(dept)
        
    response['Content-Disposition'] = 'attachment; filename="departments.csv"' 
    return response

# function export job position function to csv
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager','Staff'])
def jobposition_record(request):
    
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['JobPosition ID', 'Job Position', 'Job Description'])
    # fetch job position from database
    for position in JobPosition.objects.all().values_list('id', 'name', 'job_description'):
        writer.writerow(position)
        
    response['Content-Disposition'] = 'attachment; filename="jobposition.csv"'
    return response

# fucntion to export employee contract to csv
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager','Staff'])
def contract_record(request):
    
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Contract ID', 'Contract Ref', 'Employee ID', 'Department', 'Job Position', 'Acc No', 'Bank Name', 'Salary Type', 'Salary Details', 'Start Date', 'End Date', 'Status'])
    # fetch data from database
    for contract in EmployeeContract.objects.all().values_list('id', 'contract_reference', 'employee', 'department', 'job_position', 'acc_no', 'bank_name', 'salary_type', 'salary_details', 'start_date', 'end_date', 'status'):
        writer.writerow(contract)
        
    response['Content-Disposition'] = 'attachment; filename="employeecontract.csv"'
    return response
    