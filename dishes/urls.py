from django.urls import path
from .views import DishCreateView

urlpatterns = [
    path('create-dish/', DishCreateView.as_view(), name='create-dish'),
]
