# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_APP', '0007_auto_20180421_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='class_field',
            field=models.ForeignKey(to='BMS_APP.ClassInfo'),
        ),
        migrations.AlterField(
            model_name='classinfo',
            name='class_field',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
