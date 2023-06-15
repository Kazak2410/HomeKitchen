from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Dish
from .forms import DishForm
from django.urls import reverse_lazy


class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'create_dish.html'
    success_url = reverse_lazy('home_page')


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish_detail.html'
    context_object_name = 'dish'
    