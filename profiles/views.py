from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):

    template = 'profiles/profile.html'

    return render(request, template)
