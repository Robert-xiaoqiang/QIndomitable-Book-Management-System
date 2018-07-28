# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_APP', '0002_auto_20180419_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinfo',
            name='isbn',
        ),
    ]
