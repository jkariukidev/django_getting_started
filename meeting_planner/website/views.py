from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return render(request, "website/welcome.html",
                  {"message": "This is a template variable from the view."})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("My name is Joseph Kariuki. I am a software engineer.")
