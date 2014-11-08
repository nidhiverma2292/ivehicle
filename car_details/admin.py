from django.contrib import admin
from models import Car
# Register your models here.

class Car_admin(admin.ModelAdmin):

    list_display = ('name', 'type', 'rent', 'ac')
    search_fields = ('rent', 'name')
    list_filter = ['type', 'ac']


admin.site.register(Car, Car_admin)