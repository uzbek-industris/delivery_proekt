from django.contrib import admin
from .models import OrderInfo, Kitchen, Users

# Register your models here.
admin.site.register(OrderInfo)
admin.site.register(Kitchen)
admin.site.register(Users)