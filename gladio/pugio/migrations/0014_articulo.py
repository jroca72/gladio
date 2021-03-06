# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 17:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pugio', '0013_auto_20170329_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('ean', models.CharField(blank=True, max_length=23, null=True)),
                ('referencia', models.CharField(max_length=25)),
                ('ancho', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('fondo', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('alto', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('peso', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('volumen', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('precio_compra', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('ultimo_costo', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('fecha_alta', models.DateField(blank=True, default=datetime.datetime.now)),
                ('baja', models.BooleanField(default=False)),
                ('fecha_baja', models.DateField(blank=True, default=datetime.datetime.now)),
                ('catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pugio.catalogo')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pugio.proveedor')),
            ],
            options={
                'verbose_name_plural': 'Articulos',
            },
        ),
    ]
