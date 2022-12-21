from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'position')
    search_fields = ('fullname', )


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('dish_name', 'price')
    search_fields = ('dish_name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'served_employee', 'total_price')
    search_fields = ('client_name',)


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'count',)
    search_fields = ('name',)
