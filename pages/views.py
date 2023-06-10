from django.views.generic import ListView
from dishes.models import Dish


class HomePageView(ListView):
    model = Dish
    template_name = 'home.html'
    context_object_name = 'dish_list'
