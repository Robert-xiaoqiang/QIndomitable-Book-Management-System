# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'managed': True,
                'db_table': 'bms_app_admin',
            },
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('book_id', models.AutoField(serialize=False, primary_key=True)),
                ('book_name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=30)),
                ('isbn', models.CharField(max_length=30, db_column='ISBN', unique=True)),
                ('introduction', models.CharField(max_length=100, blank=True, null=True)),
                ('pub_date', models.DateTimeField()),
            ],
            options={
                'managed': True,
                'db_table': 'bms_app_book_info',
            },
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('borrow_id', models.AutoField(serialize=False, primary_key=True)),
                ('book', models.ForeignKey(to='BMS_APP.BookInfo')),
            ],
            options={
                'managed': True,
                'db_table': 'bms_app_borrow',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('card_id', models.AutoField(serialize=False, primary_key=True)),
                ('due_date', models.DateTimeField()),
            ],
            options={
                'managed': True,
                'db_table': 'bms_app_card',
            },
        ),
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('class_field', models.AutoField(serialize=False, primary_key=True)),
                ('class_intro', models.CharField(max_length=30, blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'bms_app_class_info',
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('reader_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50, blank=True, null=True)),
                ('occupation', models.CharField(max_length=30, blank=True, null=True)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'managed': True,
                'db_table': 'bms_app_reader',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('pass_word', models.CharField(max_length=30, blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'bms_app_user',
            },
        ),
        migrations.AddField(
            model_name='reader',
            name='user',
            field=models.ForeignKey(blank=True, null=True, to='BMS_APP.User'),
        ),
        migrations.AddField(
            model_name='card',
            name='reader',
            field=models.ForeignKey(to='BMS_APP.Reader'),
        ),
        migrations.AddField(
            model_name='borrow',
            name='card',
            field=models.ForeignKey(to='BMS_APP.Card'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='class_field',
            field=models.ForeignKey(to='BMS_APP.ClassInfo', db_column='class_id'),
        ),
        migrations.AddField(
            model_name='admin',
            name='user',
            field=models.ForeignKey(blank=True, null=True, to='BMS_APP.User'),
        ),
    ]
