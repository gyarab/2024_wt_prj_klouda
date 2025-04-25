from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    price = models.IntegerField(null=True)
    

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return f"{self.name}"

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tel = models.CharField(max_length=25, null=True)
    address = models.TextField(blank=True, default="")

    def __str__(self):
        return f"{self.name}"

class Review(models.Model):
    user = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey('Product', null=True, on_delete=models.CASCADE)
    content = models.TextField(blank=True, default="")
    stars = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user} - {self.product} - {self.stars}"

class Order(models.Model):
    user = models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    #products = models.TextField(blank=True, default="")  ??? []
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} ({self.price})"

class ImportantPPL(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    tel = models.CharField(max_length=25, null=True)

    def __str__(self):
        return f"{self.name}"

class OrderProduct(models.Model):
    order = models.ForeignKey('Order', null=True, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order}  ({self.product})"

class ProductCategory(models.Model):
    product = models.ForeignKey('Product', null=True, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return f"{self.product}  ({self.category})"

