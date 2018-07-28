
# Create your models here.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=False, max_length=30)
    pass_word = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bms_app_user'


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bms_app_admin'

class Reader(models.Model):
    reader_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'bms_app_reader'

class ClassInfo(models.Model):
    class_info_id = models.AutoField(primary_key=True, default = 0)
    class_intro = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bms_app_class_info'

class BookInfo(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    #isbn = models.CharField(db_column='ISBN', unique=True, max_length=30)  # Field name made lowercase.
    introduction = models.CharField(max_length=100, blank=True, null=True)
    pub_date = models.DateField()
    remain = models.SmallIntegerField(default = 0) #left book
    class_info = models.ForeignKey(ClassInfo)     # Field renamed because it was a Python reserved word.

    class Meta:
        managed = True
        db_table = 'bms_app_book_info'

class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    reader = models.ForeignKey(Reader)
    remain_times = models.SmallIntegerField(default = 10)
    #due_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'bms_app_card'

class Borrow(models.Model):
    borrow_id = models.AutoField(primary_key=True)
    card = models.ForeignKey(Card)
    when = models.DateTimeField(auto_now_add = True)
    book = models.ForeignKey(BookInfo)
    return_back = models.SmallIntegerField(default = 0)

    class Meta:
        managed = True
        db_table = 'bms_app_borrow'
