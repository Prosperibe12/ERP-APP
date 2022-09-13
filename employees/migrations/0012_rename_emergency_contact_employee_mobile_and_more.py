# Generated by Django 4.1 on 2022-08-31 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_rename_users_employee_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='emergency_contact',
            new_name='mobile',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='certificate_level',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='field_study',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='gender_status',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='marital_status',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='school',
        ),
    ]