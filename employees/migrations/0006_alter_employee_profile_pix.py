# Generated by Django 4.1 on 2022-08-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_alter_employeecontract_salary_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_pix',
            field=models.ImageField(blank=True, null=True, upload_to='employee_pix/'),
        ),
    ]
