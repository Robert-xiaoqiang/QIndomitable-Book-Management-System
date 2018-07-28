# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_APP', '0008_auto_20180421_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinfo',
            name='class_field',
        ),
        migrations.RemoveField(
            model_name='borrow',
            name='book',
        ),
        migrations.RemoveField(
            model_name='borrow',
            name='card',
        ),
        migrations.DeleteModel(
            name='BookInfo',
        ),
        migrations.DeleteModel(
            name='Borrow',
        ),
        migrations.DeleteModel(
            name='ClassInfo',
        ),
    ]
