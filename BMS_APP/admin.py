from django.contrib import admin
from BMS_APP.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Reader)
admin.site.register(ClassInfo)
admin.site.register(BookInfo)
admin.site.register(Borrow)
admin.site.register(Card)