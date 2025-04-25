from django.shortcuts import render
from main.models import Product

def get_homepage(request):
    context = {
        "products": Product.objects.all()
    }
    for product in context['products']:
        product.img_url = './main/pictures/'+product.image_name+'.png'
    return render(request, "main/homepage.html", context)