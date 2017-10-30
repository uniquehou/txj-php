# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-18 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('organic_name', models.CharField(blank=True, default='', max_length=100)),
                ('image', models.CharField(blank=True, default='', max_length=300)),
                ('free_course_open', models.CharField(blank=True, default='0', max_length=3)),
            ],
        ),
    ]
