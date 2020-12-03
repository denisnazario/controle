from . import serializers
from . import models
from rest_framework import generics


class BudgetList(generics.ListAPIView):
    queryset = models.Budget.objects.all()
    serializer_class = serializers.BudgetSerializer


"""
class NewsListToday(generics.ListAPIView):

    Return news publisheds today until 3 days back.

    queryset = Classificacao.objects.using(db).filter(
        date__lte=datetime.today().strftime('%Y-%m-%d'),
        date__gte=(datetime.today() - timedelta(days=3)).strftime('%Y-%m-%d')
    )

    serializer_class = ClassificacaoSerializer
"""