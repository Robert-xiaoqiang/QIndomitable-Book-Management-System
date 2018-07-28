# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_APP', '0006_searchbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='class_field',
            field=models.AutoField(db_column='class_id', serialize=False, primary_key=True),
        ),
    ]
