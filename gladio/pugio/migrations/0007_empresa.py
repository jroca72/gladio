# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pugio', '0006_auto_20170315_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=100)),
                ('cif', models.CharField(max_length=15)),
                ('direccion_social', models.CharField(max_length=150)),
                ('cp_social', models.CharField(blank=True, max_length=10, null=True)),
                ('telefono_social', models.CharField(blank=True, max_length=15, null=True)),
                ('movil_social', models.CharField(blank=True, max_length=15, null=True)),
                ('fax_social', models.CharField(blank=True, max_length=15, null=True)),
                ('mail_social', models.EmailField(blank=True, max_length=125)),
                ('web', models.URLField(blank=True, max_length=150)),
                ('logotipo', models.ImageField(blank=True, upload_to='imagenes')),
                ('nombre_comercial', models.CharField(max_length=100)),
                ('poblacion_social', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pugio.poblacion')),
                ('provincia_social', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pugio.provincia')),
            ],
            options={
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]
