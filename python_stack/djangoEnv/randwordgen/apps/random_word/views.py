from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.utils.crypto import get_random_string
import random

def index(request):
    return render(request, 'random_word/index.html')

def random_word(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    word = ''
    my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
    for times in range (0, 14):
        word = word + str(random.choice(my_letters))
    words = {
        'random_word': word
    }
    return render(request, 'random_word/index.html', words)

def reset(request):
    request.session.clear()
    return redirect('/')
