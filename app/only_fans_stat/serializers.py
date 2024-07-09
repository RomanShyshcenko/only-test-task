from rest_framework import serializers
from .models import Links, AccountDetail


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetail
        fields = '__all__'
