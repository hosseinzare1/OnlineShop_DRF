# Generated by Django 4.0.2 on 2022-02-10 14:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0003_alter_user_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 14, 49, 27, 823732, tzinfo=utc)),
        ),
    ]
