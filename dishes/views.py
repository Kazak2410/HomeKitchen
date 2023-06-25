from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Dish, Category
from .forms import DishForm
from django.urls import reverse_lazy
from django.db.models.functions import Lower


class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'create_dish.html'
    success_url = reverse_lazy('home_page')


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish_detail.html'
    context_object_name = 'dish'


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        dishes = Dish.objects.annotate(lower_name=Lower('name')).filter(lower_name__icontains=searched)

        return render(request, 'search.html', {'searched': searched, 'dishes': dishes})
    else:
        return render(request, 'search.html', {})
