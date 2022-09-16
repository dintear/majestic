from django.shortcuts import render, redirect

from .forms import *


def homepage(request):
    return render(request, 'majestic/index.html')


def about(request):
    return render(request, 'majestic/about.html')


def vyshivka_na_kroe(request):
    return render(request, 'majestic/vyshivka_na_kroe.html')


def shevrony_i_nashivki(request):
    return render(request, 'majestic/shevrony_i_nashivki.html')


def vyshivka_na_gotovyh_izdeliyah(request):
    return render(request, 'majestic/vyshivka_na_gotovyh_izdeliyah.html')


def cerkovnaya_vyshivka(request):
    return render(request, 'majestic/cerkovnaya_vyshivka.html')


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


def qna(request):
    return render(request, 'majestic/qna.html')