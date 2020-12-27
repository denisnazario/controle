from . import serializers
from . import models
from rest_framework import viewsets
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'budgets': reverse('budgets-list', request=request, format=format)
    })


class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BudgetSerializer

    def get_queryset(self):
        user = self.request.user
        return models.Budget.objects.filter(
            Q(host=user) | Q(guest=user)
        )

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AccountSerializer

    def get_queryset(self):
        user = self.request.user
        return models.Account.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CardSerializer

    def get_queryset(self):
        user = self.request.user
        return models.CreditCard.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PaymentDataViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PaymentDataSerializer

    def get_queryset(self):
        user = self.request.user
        return models.PaymentData.objects.filter(user=user)


class PaymentSplitViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PaymentSplitSerializer

    def get_queryset(self):
        user = self.request.user
        return models.PaymentSplit.objects.filter(
            Q(personal_1=user) |
            Q(personal_2=user) |
            Q(personal_3=user) |
            Q(personal_4=user) 
        )
    
    def perform_create(self, serializer):
        serializer.save(personal_1=self.request.user)


class TransactViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransactSerializer

    def get_queryset(self):
        user = self.request.user
        return models.Transact.objects.filter(
            Q(budget__host=user) | Q(budget__guest=user)
        ) 