# Generated by Django 4.1 on 2022-08-08 21:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
