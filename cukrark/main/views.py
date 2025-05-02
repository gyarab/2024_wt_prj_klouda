from django.shortcuts import render
from main.models import Product

def get_homepage(request):
    products = Product.objects.all().order_by('name')

    # filter by name if a query string is present
    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search)

    context = {
        "products": products
    }

    for product in context['products']:
        product.img_url = './main/pictures/'+product.name+'.png'
    return render(request, "main/homepage.html", context)

def get_base(request):
    context = {
    }
    return render(request, "main/base.html", context)

def get_one(request):
    context = {
    }
    return render(request, "main/one.html", context)

def get_two(request):
    context = {
    }
    return render(request, "main/two.html", context)