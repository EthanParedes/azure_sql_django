from django.utils.timezone import localtime
from rest_framework import serializers
from .models import Store, Products

class StoreSerializer(serializers.ModelSerializer):
    created_date2 = serializers.SerializerMethodField()
    updated_date2 = serializers.SerializerMethodField()

    def get_created_date2(self, obj):
        return localtime(obj.created_date2).strftime('%d/%m/%Y %H:%M:%S')

    def get_updated_date2(self, obj):
        return localtime(obj.updated_date2).strftime('%d/%m/%Y %H:%M:%S')

    class Meta:
        model = Store
        fields = ['store_id', 'store_location', 'created_date2', 'updated_date2']

class ProductSerializer(serializers.ModelSerializer):
    created_date = serializers.SerializerMethodField()
    updated_date = serializers.SerializerMethodField()

    def get_created_date(self, obj):
        return localtime(obj.created_date).strftime('%d/%m/%Y %H:%M:%S')

    def get_updated_date(self, obj):
        return localtime(obj.updated_date).strftime('%d/%m/%Y %H:%M:%S')

    class Meta:
        model = Products
        fields = ['product_id', 'product_name', 'created_date', 'updated_date']
