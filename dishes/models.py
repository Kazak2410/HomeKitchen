from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    ingredients = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("dish-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name
