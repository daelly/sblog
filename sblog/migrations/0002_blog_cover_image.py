# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-18 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover_image',
            field=models.ImageField(default=1, height_field=150, upload_to='uploads/%Y/%m/%d', width_field=215),
            preserve_default=False,
        ),
    ]
