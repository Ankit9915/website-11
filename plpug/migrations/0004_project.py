# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plpug', '0003_news_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Project name')),
                ('project_url', models.URLField(verbose_name='URL')),
            ],
        ),
    ]