# Generated by Django 5.0.4 on 2024-05-23 13:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Task with such Name already exist.'}, help_text='Obligatory field.', max_length=255, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='Describe the task.', max_length=1000, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
