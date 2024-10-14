from django.shortcuts import render
from .models import *

def build_template(lst: list, cols: int) -> list[list]:
    new_list = [lst[i:i + cols] for i in range(0,len(lst), cols)]
    return new_list


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 
                  'comp/product_list.html', 
                  context={'product_list': build_template(products, 3),
                    'categories': categories})

def product_detail(request):
    categories = Category.objects.all()
    product = Product.objects.get(pk=1)