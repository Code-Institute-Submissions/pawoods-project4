from django.shortcuts import render
from products.models import Category, SubCategory


def view_basket(request):
    """ Return the basket contents page """

    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()

    context = {
        'categories': categories,
        'sub_categories': sub_categories,
    }

    return render(request, 'basket/basket.html', context)