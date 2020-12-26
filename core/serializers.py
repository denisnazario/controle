from rest_framework import serializers
from . import models


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Budget
        fields = [
            'title',
            'host',
            'guest',
            'estimate',
            'cost'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['title', 'description']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ['title', 'bank', 'number', 'agency', 'operation']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreditCard
        fields = ['title', 'bank', 'number', 'flag']


class PaymentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaymentData
        fields = []