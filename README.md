# Enterprise Resource Plannig Application
Python/Django Resource Planning Application for Organizations.
This Application automates workflows that are form-based and approval-driven. It improves the way that information flows between people and systems. It helps organisation handles Employee and Employee related activities such as Leave Request, Employee Appraisal Employee Payroll and Organisation's Purchases.


## Modules/Apps
* WEBAPP: The organisations website is handled by this app.

* USERAPP: Employee's authentication, authorisation, password reset is handled here.

* EMPLOYEE: This module handles all HR functions within an organisation. Sub-modules under this app are;
  a.) Job Positions.
  b.) Departments.
  c.) Employees.
  d.) Employee Contracts.

* APPRAISAL: All Employee's request for appraisal are handled in this module with full approval rights for Managers.
  Employee's are appraised based on their KPI's.

* PAYROLL: This module will handle all company's payroll and batch payslip.
 
* PURCHASE: Handles all Company's Purchases. Sub-modules under this app are;
  a.) Vendors
  b.) Products
  c.) Purchase Orders.
  d.) RFQs.
  e.) Purchase Request.

* VENDORAPP: This app will handle all organisations external vendor. Vendors will be able to handle their RFQs, 
  Tender, POs and Invoices from this section.

* TEMPLATES: This folder holds the frontend view for each app.

* requirements.txt:  All external packages used for this application. 

## Requirements
* Python
* Django
* Install all packages in the requirements.txt file

## How to run the application
* clone this repository and cd inside your project root directory and create a virtual environment. 
* Run - `python -m venv ./venv` This will install your virtual environment, all dependencies will live here.
* Activate the virtual environment by using the command - `. venv/scripts/activate` 
* Install django with the following command `pip install django`
* Now open project requirement.txt file you will find the packages used for this application. Kindly `pip install` all packages in the requirements.txt file.
* Run `py manage.py makemigrations`.
* Run `py manage.py migrate`.
* Start development server by running the command `py manage.py runserver` 
* Type into your browser url the following command `localhost:8000` and the application index page will be up.

## Login admin user/password:
* Contact admin on the email below for login details
* Email: Prosperibe12@gmail.com

## Complete settings
* Got to settings.py file of erpproject
* Email setting: Set application email for sending automated emails. Kindly fill in your email details
* EMAIL_HOST_USER = 
* EMAIL_HOST_PASSWORD = 
  
  - Set your Email address for  EMAIL_HOST_USER on settings.py
  
  - Select email driver. If smtp:- 
  
    - Type email host name.[ example : for gmail `smtp.gmail.com` ]
  
    - Type the port number :- [ example : for gmail port `465` ]
    
    - Type password :- password of that email with is used as the email address.

    - Select Encryption type :- Port `465` (SSL required), Port `587` (TLS required).
                                                
**N.B:-** Be carefull about `Email Setting` which is must needed for sending auto email notification. If you don't complete the `Email Setting` some functionalities will not work properly.
* If you plan to use postgres DB with this application, Install the extension for django-postgres using the command `pip install psycopg2`.
* Uncomment the Postgres DB settings in the settings.py file and comment-out the sqlite3 settings.
* Run migration, Run this command `py manage.py makemigrations` and `py manage.py migrate`.

**N.B:-** If any issue is encountered during setting up this application, kindly email me `Prosperibe12@gmail.com`.
* This project is still on development stage.
