# Generated by Django 4.0.2 on 2022-02-08 19:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]
