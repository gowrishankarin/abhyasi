# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abhyasis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitting',
            name='date_and_time',
        ),
        migrations.AddField(
            model_name='abhyasi',
            name='email',
            field=models.EmailField(default=b'abhyasi@abhyasi.com', max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='sitting',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date of individual sitting', null=True),
        ),
        migrations.AddField(
            model_name='sitting',
            name='time',
            field=models.TimeField(auto_now_add=True, verbose_name=b'Time at which individual sitting given', null=True),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='experiences',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='findings',
            field=models.TextField(max_length=300),
        ),
    ]
