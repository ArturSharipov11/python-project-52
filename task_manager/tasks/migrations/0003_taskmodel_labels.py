# Generated by Django 5.0.4 on 2024-05-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='labels',
            field=models.ManyToManyField(
                blank=True,
                help_text='Select one or more tags.',
                to='labels.labelmodel',
                verbose_name='Labels'),
        ),
    ]
