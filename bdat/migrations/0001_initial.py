# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-05 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('source', models.TextField(null=True)),
                ('article', models.TextField(null=True)),
                ('type', models.CharField(max_length=100)),
                ('pays', models.CharField(max_length=100)),
                ('where', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('prix', models.FloatField(null=True)),
                ('mobility', models.CharField(max_length=100)),
                ('languages', models.TextField(null=True)),
                ('type_cif', models.CharField(max_length=100)),
                ('fonction', models.CharField(max_length=100)),
                ('type_environnement', models.CharField(max_length=100)),
                ('type_age', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='/img')),
                ('cat_assistance', models.CharField(max_length=100)),
                ('cat_fonctions', models.CharField(max_length=100)),
                ('cat_techno', models.CharField(max_length=100)),
                ('tags', models.TextField(null=True)),
            ],
        ),
    ]
