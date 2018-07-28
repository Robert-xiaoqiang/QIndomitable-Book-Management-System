# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_APP', '0014_card_remain_times'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SearchBook',
        ),
        migrations.AddField(
            model_name='borrow',
            name='return_back',
            field=models.SmallIntegerField(default=0),
        ),
    ]
