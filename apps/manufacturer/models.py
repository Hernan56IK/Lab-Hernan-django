from django.db import models

class Manufacturer(models.Model):
    manufacturer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        db_table = "manufacturer"  
        
    def __str__(self):
        return self.name

