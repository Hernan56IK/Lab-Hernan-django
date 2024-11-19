from django.db import models
from apps.manufacturer.models import Manufacturer

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Nuevo campo para el precio
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True)  # Clave foránea a Manufacturer
    created_at = models.DateTimeField(auto_now_add=True)  # Automáticamente asigna el timestamp de creación

    class Meta:
        db_table = "product"  
        
    def __str__(self):
        return self.name

