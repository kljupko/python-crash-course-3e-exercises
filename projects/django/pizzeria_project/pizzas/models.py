from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A pizza the pizzeria has on offer."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the pizza."""
        return self.name.title()

class Topping(models.Model):
    """A topping on a pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the topping."""
        return self.name.title()