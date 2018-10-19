from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=50, unique=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Seller {self.name}'

    def get_items(self):
        return self.items.all()
