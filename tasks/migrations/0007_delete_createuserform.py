# Generated by Django 3.2 on 2021-06-11 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_task_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CreateUserForm',
        ),
    ]
