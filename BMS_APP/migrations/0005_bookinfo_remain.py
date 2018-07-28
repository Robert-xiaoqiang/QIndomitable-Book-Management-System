# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_APP', '0004_auto_20180420_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='remain',
            field=models.SmallIntegerField(default=0),
        ),
    ]
