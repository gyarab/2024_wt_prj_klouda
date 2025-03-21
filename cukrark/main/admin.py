from django.contrib import admin
from .models import Product
from .models import Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "category"]

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(Category, CategoryAdmin)
