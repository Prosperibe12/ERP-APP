# Generated by Django 4.1 on 2022-08-17 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_alter_employee_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeecontract',
            name='salary_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
