from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, default="")

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return f"{self.name}"


