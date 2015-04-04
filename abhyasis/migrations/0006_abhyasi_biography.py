# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abhyasis', '0005_auto_20150404_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='abhyasi',
            name='biography',
            field=models.TextField(default=b'Short Bio', max_length=300),
        ),
    ]
