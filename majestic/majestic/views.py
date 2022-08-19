from django.shortcuts import render, redirect

from .forms import *


def homepage(request):
    return render(request, 'majestic/index.html')


def cost(request):
    return render(request, 'majestic/cost.html')


def contacts(request):
    """View for displaying the 'Contacts' page"""
    if request.method == 'POST':
        form = AddMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('majestic:contacts')
    else:
        form = AddMessageForm()

    context = {
        'message_form': form,
    }
    
    return render(request, 'majestic/contacts.html', context)