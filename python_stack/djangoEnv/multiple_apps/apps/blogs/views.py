from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request, number):
    response = "placeholder to display blog " + number
    return HttpResponse(response)

def edit(request, number):
    response = "placeholder to edit blog " + number
    return HttpResponse(response)

def delete(request, number):
    response = "placeholder to delete blog " + number
    return HttpResponse(response)
