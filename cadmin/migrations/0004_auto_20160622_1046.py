# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-22 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cadmin', '0003_request_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='status',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]