from django.urls import path
from .views import product_list

urlpatterns = [
    path('comp/', product_list),
]
