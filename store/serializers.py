# serializers.py
from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id', 'name', 'barcode', 'sign', 'main_unit', 'sell_price1', 'sale_tax_per',
            'main_unit_pack', 'sub_unit_pack', 'sub_unit', 'small_unit', 'item_class_id'
        ]



class ItemsClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsClass
        fields = ['id', 'name', 'tree_index', 'prev', 'is_agent']


class MobileEndUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileEndUser
        fields = [
            'id', 'user', 'phone', 'address_one', 'address_two', 'address_three',
            'address_four', 'address_five', 'address_six', 'address_seven',
            'address_eight', 'address_nine', 'address_ten'
        ]