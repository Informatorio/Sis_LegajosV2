# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-03 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('apellido', models.CharField(max_length=70)),
                ('nombre_usuario', models.CharField(db_index=True, max_length=70, unique=True)),
                ('contraseña', models.CharField(max_length=32)),
                ('is_active', models.BooleanField(default=True)),
                ('rol', models.CharField(choices=[('JAD', 'Jefe de Auxiliares'), ('AD', 'Auxiliar Docente')], max_length=3)),
            ],
        ),
    ]
