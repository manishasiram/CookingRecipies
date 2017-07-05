# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=50)),
                ('rel_date', models.DateTimeField()),
                ('genere', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hello.Genere')),
            ],
        ),
    ]
