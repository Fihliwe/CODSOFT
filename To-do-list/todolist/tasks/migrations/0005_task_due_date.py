# Generated by Django 5.1.2 on 2024-11-21 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]