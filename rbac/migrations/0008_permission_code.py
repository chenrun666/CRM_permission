# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-04 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0007_permission_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='code',
            field=models.CharField(default='1', max_length=64, verbose_name='代码'),
        ),
    ]
