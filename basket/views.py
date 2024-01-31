from django.shortcuts import render


def view_basket(request):
    """ Return the basket contents page """

    context = {

    }

    return render(request, 'basket/basket.html', context)