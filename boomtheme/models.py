from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class products(models.Model):
    name = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image1 = models.ImageField(upload_to="media_imgs")
    image2 = models.ImageField(upload_to="media_imgs")

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name


class orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    total_quantity = models.IntegerField()

    class Meta:
        db_table = "orders"

    def __str__(self):
        return self.name


class order_products(models.Model):
    order = models.ForeignKey(orders, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(products, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField()
    total_price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        db_table = "order_products"

    def __str__(self):
        return self.name
