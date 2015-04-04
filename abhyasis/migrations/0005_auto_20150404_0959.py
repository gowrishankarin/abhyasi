# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abhyasis', '0004_auto_20150404_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitting',
            name='time',
        ),
        migrations.AlterField(
            model_name='sitting',
            name='date',
            field=models.DateTimeField(verbose_name=b'Date and time of individual sitting'),
        ),
    ]
