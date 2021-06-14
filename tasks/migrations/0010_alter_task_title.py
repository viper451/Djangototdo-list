# Generated by Django 3.2 on 2021-06-11 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_remove_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='todolist', to='tasks.createuserform'),
        ),
    ]
