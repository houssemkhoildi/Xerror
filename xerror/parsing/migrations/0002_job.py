# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2020-05-01 04:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('celery_id', models.CharField(blank=True, max_length=255, null=True)),
                ('nm_status', models.CharField(default=b'no', max_length=255)),
                ('vul_status', models.CharField(default=b'no', max_length=255)),
                ('exploit_status', models.CharField(default=b'no', max_length=255)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
