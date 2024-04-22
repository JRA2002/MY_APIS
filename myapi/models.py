from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.FloatField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item