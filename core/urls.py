from django.urls import path
from . import views


budget_list = views.BudgetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
budget_detail = views.BudgetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', views.api_root),
    path('budgets/', budget_list, name='budget-list'),
    path('budgets/<int:pk>/', budget_detail, name='budget-detail')
]
