# Generated by Django 3.2 on 2021-06-07 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_completetask_task_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='completetask',
        ),
    ]
