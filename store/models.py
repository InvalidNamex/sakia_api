# models.py
from django.db import models

class Item(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='ID')
    name = models.CharField(max_length=100, db_column='Name', null=True, blank=True)
    sign = models.CharField(max_length=30, db_column='Sign', null=True, blank=True)
    item_class_id = models.BigIntegerField(db_column='itemclassId', null=True, blank=True)
    barcode = models.CharField(max_length=30, db_column='BarCode', null=True, blank=True)
    main_unit = models.CharField(max_length=25, db_column='MainUnit', null=True, blank=True)
    sub_unit = models.CharField(max_length=25, db_column='SubUnit', null=True, blank=True)
    small_unit = models.CharField(max_length=25, db_column='SmallUnit', null=True, blank=True)
    main_unit_pack = models.FloatField(db_column='MainUnitPack', null=True, blank=True)
    sub_unit_pack = models.FloatField(db_column='SubUnitPack', null=True, blank=True)
    sale_tax_per = models.FloatField(db_column='SaleTaxPer', null=True, blank=True)
    sell_price1 = models.FloatField(db_column='SellPrice1', null=True, blank=True)

    class Meta:
        db_table = 'items'


class ItemsClass(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='ID')
    name = models.CharField(max_length=100, db_column='Name', null=True, blank=True)
    tree_index = models.CharField(max_length=500, db_column='TreeIndex', null=True, blank=True)
    prev = models.CharField(max_length=100, db_column='prev', null=True, blank=True)
    is_agent = models.BooleanField(db_column='isAgent', null=True, blank=True)

    class Meta:
        db_table = 'ItemsClass'


class MobileEndUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address_one = models.CharField(max_length=2000, null=True, blank=True)  # Change to CharField
    address_two = models.CharField(max_length=2000, null=True, blank=True)
    address_three = models.CharField(max_length=2000, null=True, blank=True)
    address_four = models.CharField(max_length=2000, null=True, blank=True)
    address_five = models.CharField(max_length=2000, null=True, blank=True)
    address_six = models.CharField(max_length=2000, null=True, blank=True)
    address_seven = models.CharField(max_length=2000, null=True, blank=True)
    address_eight = models.CharField(max_length=2000, null=True, blank=True)
    address_nine = models.CharField(max_length=2000, null=True, blank=True)
    address_ten = models.CharField(max_length=2000, null=True, blank=True)

    class Meta:
        db_table = 'MobileEndUsers'