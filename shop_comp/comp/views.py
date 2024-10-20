from django.shortcuts import render
from .models import *
from django.db.models import Q

def build_template(lst: list, cols: int) -> list[list]:
    new_list = [lst[i:i + cols] for i in range(0,len(lst), cols)]
    return new_list


def product_list(request):
    categories = Category.objects.all()
    search_query = request.GET.get('search', None)
    if search_query:
        products = Product.objects.filter(
            Q(title__icontains=search_query)
            |
            Q(info__icontains=search_query)
        )
    return render(request, 
                  'comp/product_list.html', 
                  context={'product_list': build_template(products, 3),
                    'categories': categories})


def product_detail(request, pk):
    categories = Category.objects.all()
    product = Product.objects.get(pk=pk)
    return render(request, 'comp/product_detail.html', context={'product': product, 'categories': categories})


def category_detail(request, pk):
    categories = Category.objects.all()
    category = Category.objects.get(pk=pk)
    products = category.products.all()
    return render (request, 'comp/category_detail.html', 
                   context={
                       'category': category, 
                       'categories': categories,
                       'product_list': build_template(products, 3),
                       })