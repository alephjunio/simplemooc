# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170720_1416'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Enrollment',
        ),
    ]