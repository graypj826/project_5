# Generated by Django 2.1 on 2018-08-21 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srvvrs', '0002_auto_20180821_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thread_id',
        ),
    ]