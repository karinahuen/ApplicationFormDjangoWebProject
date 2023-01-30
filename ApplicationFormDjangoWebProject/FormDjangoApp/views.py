from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "FormDjangoApp/index.html", 
        {
            'title' : "Application Form",
            'message' : "Application Form Demo!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "FormDjangoApp/about.html",
        {
            'title' : "About The Application Form",
            'content' : "This project is for the application form testing."
        }
    )

def create(request):
    return render(
        request,
        "FormDjangoApp/create.html",
        {
            'title' : "Create New Application Form",
            'content' : "Please fill in the form below:"
        }
    )


def history(request):
    return render(
        request,
        "FormDjangoApp/history.html",
        {
            'title' : "history The Application Form",
            'content' : "This project is for the application form testing."
        }
    )


def dateTime(request):
    now = datetime.now()

    return render(
        request,
        "FormDjangoApp/dateTime.html",
        {
            'time_now' :  now.strftime("%A, %d %B, %Y at %X")
        }
    )
