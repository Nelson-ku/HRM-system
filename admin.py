from django.contrib import admin
# from accounts.models import Customer, Product, Tag, Order, Leave

# Register your models here.

from .models import *

admin.site.register(Customer)
# admin.site.register(Tag)
# admin.site.register(Leave)
admin.site.register(Employee)
admin.site.register(Modules)
admin.site.register(Tasks)
admin.site.register(Healthinfo)

