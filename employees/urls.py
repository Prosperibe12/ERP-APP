from django.urls import path
from . import views
# from django.views.i18n import JavaScriptCatalog

"""
All urls for the users section of this application will be registered here
"""
app_name = 'employee'

urlpatterns = [
    path('create-department/', views.dept_create, name='create-dept'),
    path('department-list/', views.dept_index, name='department-list'),
    path('department-view/<str:id>/', views.dept_view, name='dept-view'),
    path('department-delete/<str:id>/', views.dept_delete, name='dept-delete'),
    path('job-position-create/', views.create_position, name='create-position'),
    path('job-position-list/', views.job_position, name='job-list'),
    path('job-position-view/<str:id>/', views.view_position, name='view-position'),
    path('job-position-delete/<str:id>/', views.delete_position, name='delete-position'),
    path('employee-list/', views.employee_index, name='employee-list'),
    path('department-details/<str:id>/', views.dept_details, name='dept-details'),
    path('create-employee/', views.employee_create, name='create-employee'),
    path('employee-view/<str:id>/', views.employee_view, name='employee-view'),
    path('employee-contract/', views.contract_index, name='list-contract'),
    path('create-contract/', views.create_contract, name='create-contract'),
    path('contract-view/<str:id>/', views.contract_view, name='view-contract'),
    path('csv-employee', views.employee_record, name='csv-employee'),
    path('csv-dept', views.dept_record, name='csv-dept'),
    path('csv-jobposition', views.jobposition_record, name='csv-jobposition'),
    path('csv-employeecontract', views.contract_record, name='csv-employeecontract'),
    # path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog')
]