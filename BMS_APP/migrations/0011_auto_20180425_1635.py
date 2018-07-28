# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_APP', '0010_auto_20180421_0059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classinfo',
            old_name='class_field',
            new_name='class_field_id',
        ),
    ]
