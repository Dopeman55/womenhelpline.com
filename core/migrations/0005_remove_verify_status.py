# Generated by Django 3.2.8 on 2021-11-05 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_verify'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verify',
            name='Status',
        ),
    ]
