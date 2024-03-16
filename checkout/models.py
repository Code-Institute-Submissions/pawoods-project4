import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address_1 = models.CharField(max_length=40, null=False, blank=False)
    street_address_2 = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=40, null=False, blank=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """ Generate a random, unique order number """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update order total based on line items """
        self.total = self.lineitems.aggregate(Sum('line_total'))['line_total__sum']
        self.save()

    def save(self, *args, **kwargs):
        """ Overide the save method and set order number if none set """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_total = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """ Overide the save method, set line total and update order total """

        self.line_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
