# Generated by Django 5.0.6 on 2024-06-17 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_label'),
        ('tasks', '0004_task_remove_taskmodel_author_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LabelModel',
        ),
    ]
