# coding=utf-8
from rest_framework import serializers
from models import Product
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    price = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

    # 检查product是否已经存在
    def validate_name(self, value):
        if Product.objects.filter(name=value).exists():
            raise serializers.ValidationError("Product have existed")
        else:
            return value


class CartSerializer(serializers.Serializer):
    pass