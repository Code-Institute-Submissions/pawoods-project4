from django.shortcuts import render
from .models import Update

def index(request):
    """ Return the index page """

    updates = Update.objects.all()

    context = {
        'updates': updates,
    }

    return render(request, 'home/index.html', context)
