# Generated by Django 4.1 on 2023-05-28 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcources', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessons',
            name='icon',
        ),
    ]
