# Generated by Django 3.2.7 on 2021-09-22 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='person',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]
