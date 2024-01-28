from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, SubCategory


def all_products(request):
    """ Show all products, sorting and search queries """

    products = Product.objects.all()
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()

    query = None
    category = None
    sub_category = None

    if request.GET:
        if 'category' in request.GET:
            selected_category = request.GET['category']
            """ Gets a list of the sub categories of the selected category """
            selected_subcats = list(sub_categories.filter(category__name=selected_category).values_list('name', flat=True))
            """ filters the product query set based on the sub categories list """
            products = products.filter(sub_category__name__in=selected_subcats)
            category = categories.filter(name=selected_category)

        if 'sub_category' in request.GET:
            selected_subcat = request.GET['sub_category']
            products = products.filter(sub_category__name=selected_subcat)
            sub_category = sub_categories.filter(name=selected_subcat)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria entered.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'categories': categories,
        'sub_categories': sub_categories,
        'search_term': query,
        'current_category': category,
        'current_subcat': sub_category,
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
