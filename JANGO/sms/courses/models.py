from django.db import models

# Create your models here.
class sales(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name