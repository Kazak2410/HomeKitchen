from django.urls import path
from .views import DishCreateView, DishDetailView

urlpatterns = [
    path('create-dish/', DishCreateView.as_view(), name='create-dish'),
    path('dish-detail/<slug:slug>/', DishDetailView.as_view(), name='dish-detail')
]
