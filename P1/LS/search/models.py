from django.db import models
from .managers import SearchManager

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Search(models.Model):
    name = models.CharField(max_length=255)
    # Campo histórico de texto (se mantiene por compatibilidad)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.JSONField(default=list)

    # Nuevo campo normalizado (FK opcional)
    category_fk = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL, related_name="products"
    )

    objects = SearchManager()

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Search, on_delete=models.CASCADE, related_name="image_set")
    url = models.URLField()
    alt = models.CharField(max_length=150, blank=True, default="")

    def __str__(self):
        return f"{self.product.name} - {self.url}"
