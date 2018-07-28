# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_APP', '0009_auto_20180421_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=30)),
                ('introduction', models.CharField(max_length=100, blank=True, null=True)),
                ('pub_date', models.DateField()),
                ('remain', models.SmallIntegerField(default=0)),
            ],
            options={
                'db_table': 'bms_app_book_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('borrow_id', models.AutoField(primary_key=True, serialize=False)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(to='BMS_APP.BookInfo')),
                ('card', models.ForeignKey(to='BMS_APP.Card')),
            ],
            options={
                'db_table': 'bms_app_borrow',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('class_field', models.AutoField(primary_key=True, serialize=False)),
                ('class_intro', models.CharField(max_length=30, blank=True, null=True)),
            ],
            options={
                'db_table': 'bms_app_class_info',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='class_field',
            field=models.ForeignKey(to='BMS_APP.ClassInfo'),
        ),
    ]
