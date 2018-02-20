from django.shortcuts import render, HttpResponse

# Create your views here.
def index(reqeust):
    return HttpResponse("Shell Queries")
