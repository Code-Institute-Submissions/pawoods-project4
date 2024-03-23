from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Update
from .forms import UpdateForm

def index(request):
    """ Return the index page """

    updates = Update.objects.all()

    context = {
        'updates': updates,
    }

    return render(request, 'home/index.html', context)


@login_required
def add_update(request):
    """ Adds update post to the home screen """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to add update posts.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Update post updated successfully')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add update post, please check the form is valid')
    else:
        form = UpdateForm()

    template = 'products/add_update.html'
    context = {
        'form': form,
    }

    return render(request, template, context)