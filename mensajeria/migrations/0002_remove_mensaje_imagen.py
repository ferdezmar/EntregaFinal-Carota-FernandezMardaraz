# Generated by Django 4.1.2 on 2022-11-01 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='imagen',
        ),
    ]
