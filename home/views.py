from django.shortcuts import render
from products.models import Category, SubCategory


def index(request):
    """ Return the index page """

    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()

    context = {
        'categories': categories,
        'sub_categories': sub_categories,
    }

    return render(request, 'home/index.html', context)
