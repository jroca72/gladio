# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 12:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pugio', '0004_cliente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'Clientes'},
        ),
    ]