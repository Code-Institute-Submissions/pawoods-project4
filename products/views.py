from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """ Show product detail page using the pk of the clicked product """

    product = get_object_or_404(Product, pk=product_id)

    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()

    context = {
        'product': product,
        'categories': categories,
        'sub_categories': sub_categories,
    }

    return render(request, 'products/product_detail.html', context)
