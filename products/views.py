from django.shortcuts import render
from .models import Product, Category, SubCategory


def all_products(request):
    """ Show all products, sorting and search queries """

    categories = Category.objects.all()
    products = Product.objects.all()
    sub_categories = SubCategory.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'sub_categories': sub_categories,
    }

    return render(request, 'products/products.html', context)
