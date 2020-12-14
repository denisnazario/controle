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