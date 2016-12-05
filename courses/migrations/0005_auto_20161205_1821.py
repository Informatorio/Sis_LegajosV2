# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-05 21:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_remove_course_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='course',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='course',
            name='nombre_usuario',
        ),
        migrations.RemoveField(
            model_name='course',
            name='password',
        ),
        migrations.AddField(
            model_name='course',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
