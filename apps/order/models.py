from django.db import models
from apps.clients.models import Customer

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)  
    order_date = models.DateTimeField(auto_now_add=True) 

    class Meta:
        db_table = "order"  
        
    def __str__(self):
        return f"{self.order_id}"

