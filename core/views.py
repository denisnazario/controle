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
