# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abhyasis', '0002_auto_20150404_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitting',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date of individual sitting'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='time',
            field=models.TimeField(auto_now_add=True, verbose_name=b'Time at which individual sitting given'),
        ),
    ]
