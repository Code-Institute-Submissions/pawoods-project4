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
    """ Adds post to the home screen """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to add posts.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Post updated successfully')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add post, please check the form is valid')
    else:
        form = UpdateForm()

    template = 'home/add_update.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_update(request, update_id):
    """ Edit post using the id clicked on """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to delete posts.')
        return redirect(reverse('home'))
    update = get_object_or_404(Update, pk=update_id)
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=update)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to update post, please check the form is valid')
    else:
        form = UpdateForm(instance=update)
        messages.info(request, f'You are editing post with title: {update.title}.')

    template = 'home/update_update.html'
    context = {
        'form': form,
        'update': update,
    }

    return render(request, template, context)


@login_required
def delete_update(request, update_id):
    """ Delete the post using the id clicked on """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to delete post')
        return redirect(reverse('home'))

    update = get_object_or_404(Update, pk=update_id)
    update.delete()
    messages.success(request, 'Post Deleted!')
    return redirect(reverse('home'))