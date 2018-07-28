# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_APP', '0003_remove_bookinfo_isbn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='due_date',
        ),
        migrations.AddField(
            model_name='borrow',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 20, 11, 3, 59, 310722, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
