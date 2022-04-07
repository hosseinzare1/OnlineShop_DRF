# Generated by Django 4.0.2 on 2022-02-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0006_alter_user_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=30, null=True),
        ),
    ]