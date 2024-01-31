from .models import Category, SubCategory

def menu_categories(request):

    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()

    context = {
        'categories': categories,
        'sub_categories': sub_categories,
    }

    return context