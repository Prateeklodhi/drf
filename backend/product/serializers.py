from rest_framework import serializers
from .models import Product
class ProductSerialier(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        fields = ['id','title','price','content','sale_price','my_discount']

    def get_my_discount(self,obj):
        print(obj.id)
        return obj.get_discount()