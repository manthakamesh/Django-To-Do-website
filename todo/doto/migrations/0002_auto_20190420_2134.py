# Generated by Django 2.1.2 on 2019-04-20 16:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
