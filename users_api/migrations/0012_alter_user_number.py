# Generated by Django 4.0.2 on 2022-04-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0011_remove_user_des_alter_user_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.IntegerField(blank=True, unique=True),
        ),
    ]