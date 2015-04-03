# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abhyasi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('id_card_number', models.CharField(max_length=12)),
                ('date_of_birth', models.DateField(verbose_name=b'Date of Birth')),
                ('date_of_join', models.DateField(verbose_name=b'Date of Join')),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sitting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_and_time', models.DateTimeField(verbose_name=b'Date and Time of Individual Sitting')),
                ('findings', models.CharField(max_length=300)),
                ('experiences', models.CharField(max_length=300)),
                ('name', models.ForeignKey(to='abhyasis.Abhyasi')),
            ],
        ),
    ]
