# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_APP', '0011_auto_20180425_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='class_field_id',
            field=models.AutoField(primary_key=True, db_column='class_field', serialize=False),
        ),
    ]
