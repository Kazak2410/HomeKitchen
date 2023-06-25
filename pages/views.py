from typing import Any, Dict
from django.views.generic import ListView, TemplateView
from dishes.models import Dish, Category


class MenuPageView(ListView):
    model = Dish
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish_list'] = Dish.objects.all()
        context['dish_category'] = Category.objects.all()
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'


class HomePageView(ListView):
    model = Dish
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish_list'] = Dish.objects.all()
        context['dish_category'] = Category.objects.all()
        return context
