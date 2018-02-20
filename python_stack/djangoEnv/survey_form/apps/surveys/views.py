from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    request.session['counter'] = request.session.get('counter', 0)
    return render(request, "surveys/index.html")


def surveys(request):
    if request.method == "POST":
        request.session['counter'] += 1;
        #### COULD DO THIS ###
        # request.session['name'] = request.POST['name']
        # request.session['location'] = request.POST['location']
        # request.session['language'] = request.POST['language']
        # request.session['comments'] = request.POST['comments']

        for key, value in request.POST.iteritems():
            if not key == "csrfmiddlewaretoken":
                request.session[key] = value


        return redirect('/results')

    else:
        return redirect('/')


def results(request):
    return render(request, 'surveys/results.html')
