# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ManyToManyField(to='app.SimplePlace')),
            ],
        ),
    ]