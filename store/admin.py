# admin.py
from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'barcode', 'sign', 'main_unit', 'sell_price1', 'item_class_id'
    )
    search_fields = ('name', 'barcode', 'sign')
    list_filter = ('main_unit', 'item_class_id')
    
    fieldsets = (
        (None, {
            'fields': ('name', 'sign', 'barcode', 'item_class_id')
        }),
        ('Pricing & Stock', {
            'fields': ('sell_price1', 'sale_tax_per')
        }),
        ('Units & Packaging', {
            'fields': ('main_unit', 'main_unit_pack', 'sub_unit', 'sub_unit_pack', 'small_unit')
        }),
    )
