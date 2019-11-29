from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)  # Regular & Sicilian

    def __str__(self):
        return f"{self.name}"


class Size(models.Model):
    size = models.IntegerField()  # Cheese=0, 1-3, Special=5

    def __str__(self):
        return f"{self.size}"


class Pizza(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="pizza_category")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="pizza_size")  # TODO bad naming choice
    small = models.DecimalField(max_digits=4, decimal_places=2)  # price in $
    large = models.DecimalField(max_digits=4, decimal_places=2)  # price in $

    def __str__(self):
        topping = f"Cheese" if f"{self.size}" == "0" else f"{self.size} toppings"  # TODO there must be a better way
        return f"{self.category} : {topping} - small: {self.small} $ // large: {self.large} $"


class Toppings(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping}"
