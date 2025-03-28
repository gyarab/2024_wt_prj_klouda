from django.contrib import admin
from .models import Product
from .models import Category
from .models import User
from .models import Order
from .models import Review
from .models import ImportantPPL

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "category"]

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

class ImportantPPLAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "position", "email"]

admin.site.register(ImportantPPL, ImportantPPLAdmin)

