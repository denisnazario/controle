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
category_list = views.CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
category_detail = views.CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

account_list = views.AccountViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

account_detail = views.AccountViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update'
})

card_list = views.CardViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

card_detail = views.CardViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update'
})

payment_data_detail = views.PaymentDataViewSet.as_view({
    'delete': 'destroy'
})

payment_split_list = views.PaymentSplitViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

payment_split_detail = views.PaymentSplitViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', views.api_root),
    path('budgets/', budget_list, name='budget-list'),
    path('budgets/<int:pk>/', budget_detail, name='budget-detail'),
    path('categories/', category_list, name='category-list'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),
    path('payment-data/account/', account_list, name='account-list'),
    path('payment-data/account/<int:pk>/', account_detail, name='account-detail'),
    path('payment-data/card/', card_list, name='card-list'),
    path('payment-data/card/<int:pk>/', card_detail, name='card-detail'),
    path('payment-data/<int:pk>/', payment_data_detail, name='payment-data-detail'),
    path('payment-split/', payment_split_list, name='payment-split-list'),
    path('payment-split/<int:pk>/', payment_split_detail, name='payment-split-detail')
]
