from .models import Category, SubCategory, Brand

def menu_categories(request):

    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    brands = Brand.objects.all()

    context = {
        'categories': categories,
        'sub_categories': sub_categories,
        'brands': brands,
    }

    return context