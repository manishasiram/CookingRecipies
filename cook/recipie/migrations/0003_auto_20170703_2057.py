# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 20:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipie', '0002_auto_20170703_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories_sub_categories_map',
            old_name='sub_category_id',
            new_name='subcategory_id',
        ),
        migrations.RenameField(
            model_name='recipie_recipie_subtype_map',
            old_name='R_subtype_id',
            new_name='Rsubtype_id',
        ),
        migrations.RenameField(
            model_name='recipie_subtype',
            old_name='recipie_subtype_name',
            new_name='recipie_subtypename',
        ),
        migrations.RenameField(
            model_name='recipies_rmap_cmap',
            old_name='C_map_id',
            new_name='Cmap_id',
        ),
        migrations.RenameField(
            model_name='recipies_rmap_cmap',
            old_name='R_map_id',
            new_name='Rmap_id',
        ),
        migrations.RenameField(
            model_name='sub_categories',
            old_name='sub_categorie_name',
            new_name='subcategorie_name',
        ),
    ]
