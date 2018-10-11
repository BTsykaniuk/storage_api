from django.db import models


class Product(models.Model):
    name = models.CharField('name', max_length=50)
    description = models.TextField('Description', max_length=500, null=True, blank=True)
    date_added = models.DateField('Added', auto_now_add=True, editable=False)
    date_updated = models.DateField('Updated', auto_now=True, null=True, blank=True)
