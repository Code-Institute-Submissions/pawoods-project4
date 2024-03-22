from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, SubCategory, Brand
from .forms import ProductForm

from profiles.models import WishList, UserProfile


def all_products(request):
    """ Show all products, sorting and search queries """

    products = Product.objects.all()
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    brands = Brand.objects.all()

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            wish_list = list(profile.wishlist.all().values_list('product', flat=True))
        except UserProfile.DoesNotExist:
            profile = None
            wish_list = None

        for product in products:
            if product.id in wish_list:
                product.is_liked = True

    query = None
    category = None
    sub_category = None
    brand = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey == 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                """ Gets category name through the sub_category of the product """
                sortkey = 'sub_category__category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)


        if 'category' in request.GET:
            selected_category = request.GET['category']
            """ Gets a list of the sub categories of the selected category """
            selected_subcats = list(sub_categories.filter(category__name=selected_category).values_list('name', flat=True))
            """ filters the product query set based on the sub categories list """
            products = products.filter(sub_category__name__in=selected_subcats)
            category = categories.get(name=selected_category)

        if 'sub_category' in request.GET:
            selected_subcat = request.GET['sub_category']
            products = products.filter(sub_category__name=selected_subcat)
            sub_category = sub_categories.get(name=selected_subcat)
        
        if 'brand' in request.GET:
            selected_brand = request.GET['brand']
            products = products.filter(brand__name=selected_brand)
            brand = brands.get(name=selected_brand)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria entered, displaying all products")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
        'current_subcat': sub_category,
        'current_brand': brand,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Show product detail page using the pk of the clicked product """

    product = get_object_or_404(Product, pk=product_id)
    brand = product.brand
    sub_category = product.sub_category
    related_products = None
    if brand:
        related_products = Product.objects.filter(brand=brand, sub_category=sub_category).exclude(pk=product_id)
        if not related_products:
            related_products = Product.objects.filter(sub_category=sub_category).exclude(pk=product_id)
    else:
        related_products = Product.objects.filter(sub_category=sub_category).exclude(pk=product_id)

    context = {
        'product': product,
        'related_products': related_products,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Adds product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete the product using the id clicked on """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to delete products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product Deleted!')
    return redirect(reverse('products'))
