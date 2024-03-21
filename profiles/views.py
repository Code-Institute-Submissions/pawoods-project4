from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile': True,
    }

    return render(request, template, context)


@login_required
def wish_list(request, item_id):
    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=item_id)

    wish_list = WishList.objects.get(product=product, profile=profile)

    if wish_list.exists:
        wish_list.delete()
    else:
        wish_list_instance = WishList.objects.create(
            profile=profile,
            product=product,
        )