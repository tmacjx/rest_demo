# coding=utf-8
from rest_framework import serializers
from models import User


class LoginSerializer(serializers.models):
    class Meta:
        model = User


class UserSerializer(serializers.models):
    class Meta:
        model = User
