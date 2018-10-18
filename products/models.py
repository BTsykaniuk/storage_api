from datetime import datetime
from django.db import models


class Product(models.Model):
    name = models.CharField('name', max_length=50)
    description = models.TextField('Description', max_length=500, null=True, blank=True)
    date_added = models.DateField('Added', auto_now_add=True, editable=False)
    date_updated = models.DateField('Updated', null=True, blank=True, default=None)

    def __str__(self):
        return f'Product - {self.name}'

    # def save(self, *args, **kwargs):
    #     """
    #     Custom check if product modified. If updated=True -> add date_updated
    #     """
    #     updated = False
    #     if self.pk is not None:
    #         orig = Product.objects.get(pk=self.pk)
    #         field_names = [field.name for field in Product._meta.fields]
    #         for field_name in field_names:
    #             field_stat = getattr(orig, field_name) != getattr(self, field_name)
    #             if field_stat:
    #                 updated = True
    #                 break
    #     if updated:
    #         self.date_updated = datetime.today().date()
    #
    #     super(Product, self).save(*args, **kwargs)
