from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(
            request, "Your basket is currently empty"
        )
        return redirect(reverse('products'))

    template = 'checkout/checkout.html'

    return render(request, template)
