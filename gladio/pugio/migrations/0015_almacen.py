# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pugio', '0014_articulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cp', models.CharField(blank=True, max_length=10, null=True)),
                ('pais', models.CharField(blank=True, default='espana', max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('movil', models.CharField(blank=True, max_length=15, null=True)),
                ('fax', models.CharField(blank=True, max_length=15, null=True)),
                ('correo', models.EmailField(blank=True, max_length=125)),
                ('responsable', models.CharField(blank=True, max_length=50)),
                ('exposicion', models.BooleanField(default=False)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pugio.empresa')),
                ('poblacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pugio.poblacion')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pugio.provincia')),
            ],
            options={
                'verbose_name_plural': 'Almacenes',
            },
        ),
    ]
