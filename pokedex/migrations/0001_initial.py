# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('english_full_name', models.CharField(max_length=255)),
                ('japanese_full_name', models.CharField(max_length=255)),
                ('primary_type', models.IntegerField()),
                ('secondary_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]