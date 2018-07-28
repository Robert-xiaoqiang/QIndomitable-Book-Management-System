# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_APP', '0005_bookinfo_remain'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchBook',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('book_name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=30)),
                ('pub_date', models.DateField()),
                ('class_intro', models.CharField(max_length=30)),
            ],
        ),
    ]
