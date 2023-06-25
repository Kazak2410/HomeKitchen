from django.urls import path
from .views import HomePageView, AboutPageView, MenuPageView

urlpatterns = [
    path('menu/', MenuPageView.as_view(), name='menu_page'),
    path('about/', AboutPageView.as_view(), name='about_page'),
    path('', HomePageView.as_view(), name='home_page')
]
