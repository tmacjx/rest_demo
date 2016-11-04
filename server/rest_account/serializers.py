# coding=utf-8
from rest_framework import serializers
from models import Product, Cart
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class SignUpSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super(SignUpSerializer, self).create(validated_data)
        # 初始化一个cart
        Cart.objects.create(user=user)
        return user

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


class CartSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #      # TODO 新增product
    #      pass

    class Meta:
        model = Cart
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     # 关联用户的cart 超链接
#     cart = CartSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'cart')

class UserSerializer(serializers.ModelSerializer):
    # 关联用户的cart 超链接

    class Meta:
        model = User
        fields = '__all__'




