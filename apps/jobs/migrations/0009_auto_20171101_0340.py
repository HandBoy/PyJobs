# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20170919_2237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-data_adicionado'], 'verbose_name': 'Vaga', 'verbose_name_plural': 'Vagas'},
        ),
        migrations.AddField(
            model_name='job',
            name='home_office',
            field=models.BooleanField(default=False, verbose_name='Aceita home office'),
        ),
    ]
