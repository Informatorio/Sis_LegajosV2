# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20161205_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='apellido',
            field=models.CharField(default='apellido', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='nombre',
            field=models.CharField(default='nombre', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='nombre_usuario',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='password',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
