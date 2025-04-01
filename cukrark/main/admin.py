from django.contrib import admin
from .models import Product, Category, User, Order, Review, ImportantPPL, OrderProduct, ProductCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price"]

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

admin.site.register(Category, CategoryAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]

admin.site.register(User, UserAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "price"]

admin.site.register(Order, OrderAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product", "stars"]

admin.site.register(Review, ReviewAdmin)

class ImportantPPLAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "position", "email"]

admin.site.register(ImportantPPL, ImportantPPLAdmin)

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "product"]

admin.site.register(OrderProduct, OrderProductAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "category"]

admin.site.register(ProductCategory, ProductCategoryAdmin)

