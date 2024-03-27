from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, WishList
from .forms import UserProfileForm
from products.models import Product


@login_required
def profile(request):
    """
    A View to show the user profile with order histoy,
    details and wish list
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Failed to update profile, please check the form is valid')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    wish_list = profile.wishlist.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'wish_list': wish_list,
        'on_profile': True,
    }

    return render(request, template, context)


@login_required
def wish_list(request, product_id):
    """ Add or remove items clicked on to the user wish list """
    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    try:
        wish_list = WishList.objects.get(product=product, profile=profile)
    except WishList.DoesNotExist:
        wish_list = None    

    if wish_list:
        wish_list.delete()
        messages.info(request, 'Removed from your Wish List')
    else:
        wish_list_instance = WishList.objects.create(
            profile=profile,
            product=product,
        )
        messages.info(request, 'Added to your Wish List')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        