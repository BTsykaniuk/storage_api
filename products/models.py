from datetime import datetime
from django.db import models


class Product(models.Model):
    name = models.CharField('name', max_length=50)
    description = models.TextField('Description', max_length=500, null=True, blank=True)
    seller = models.ForeignKey(to='sellers.Seller', on_delete=models.CASCADE)
    date_added = models.DateField('Added', auto_now_add=True, editable=False)
    date_updated = models.DateField('Updated', null=True, blank=True, default=None)

    def __str__(self):
        return f'Product - {self.name}'
