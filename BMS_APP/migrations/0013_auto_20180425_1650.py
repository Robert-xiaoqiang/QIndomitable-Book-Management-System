# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_APP', '0012_auto_20180425_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='class_field',
            new_name='class_info',
        ),
        migrations.RemoveField(
            model_name='classinfo',
            name='class_field_id',
        ),
        migrations.AddField(
            model_name='classinfo',
            name='class_info_id',
            field=models.AutoField(primary_key=True, serialize=False, default=0),
        ),
    ]
