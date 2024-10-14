from django.shortcuts import render
from .models import Product, Category

def build_template(lst: list, cols: int) -> list[list]:
    new_list = [lst[i:i + cols] for i in range(0,len(lst), cols)]
    return new_list


def product_list(request):
    products = Product.objects.all()
    return render(request, 
                  'comp/product_list.html', 
                  context={'product_list': build_template(products, 3)})

def category_list(request):
    categories = Category.objects.all
    return categories