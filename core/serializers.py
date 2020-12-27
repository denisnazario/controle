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


class PaymentSplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaymentSplit
        fields = [
            'title',
            'personal_1',
            'percentage_1',
            'personal_2',
            'percentage_2',
            'personal_3',
            'percentage_3',
            'personal_4',
            'percentage_4'
        ]


class TransactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transact
        fields = [
            'title',
            'description',
            'date',
            'value',
            'parceled_out',
            'parceled_times',
            'parceled_freq',
            'payment_meth',
            'paid',
            'date_paid',
            'payment_split',
            'payment_data',
            'category',
            'budget'
        ]