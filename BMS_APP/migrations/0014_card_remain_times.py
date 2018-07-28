# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_APP', '0013_auto_20180425_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='remain_times',
            field=models.SmallIntegerField(default=10),
        ),
    ]
