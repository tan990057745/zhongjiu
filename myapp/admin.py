from django.contrib import admin

# Register your models here.
from .models import Goods, Users
admin.site.register(Goods)
admin.site.register(Users)