# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abhyasis', '0003_auto_20150404_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitting',
            name='date',
            field=models.DateTimeField(verbose_name=b'Date of individual sitting'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='time',
            field=models.TimeField(verbose_name=b'Time at which individual sitting given'),
        ),
    ]
