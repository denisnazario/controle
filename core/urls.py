from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('budget/', views.BudgetList.as_view()),
    path('auth/', obtain_jwt_token)
]