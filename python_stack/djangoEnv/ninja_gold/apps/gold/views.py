from django.shortcuts import render, redirect
from datetime import datetime
import random

# Create your views here.
def index(request):
    request.session['total'] = request.session.get('total', 0)
    return render(request, 'gold/index.html')

def process_money(request, building_type):
    this_gold = 0
    action = 'earned'
    if building_type == 'farm':
        this_gold = random.randrange(10, 21)
    elif building_type == 'cave':
        this_gold = random.randrange(5, 11)
    elif building_type == 'house':
        this_gold = random.randrange(2, 6)
    else:
        this_gold = random.randrange(-50, 51)
        if this_gold < 0:
            action = 'lost'

    timestamp = datetime.now().strftime("%Y/%m/%d %-I:%M%p")
    this_log = {
        'class': action,
        'message': "You {} {} golds from the {} ({})".format(action, this_gold, building_type, timestamp)
    }

    try:
        log_list = request.session['logs']
    except KeyError:
        log_list = []

    request.session['total'] += this_gold

    log_list.append(this_log)
    request.session['logs'] = log_list

    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
