from django.forms import ModelForm
from .models import Dish


class DishForm(ModelForm):
    class Meta():
        model = Dish
        fields = ('name', 'description', 'ingredients',
                  'category', 'price', 'image')
