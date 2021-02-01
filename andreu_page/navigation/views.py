from django.shortcuts import render
from django.http import HttpResponse
import datetime


def home(request):
    now = datetime.datetime.now()
    html = "<html><body> <h1> HOME PAGE </h1> <br> It is now %s.</body></html>" % now
    return HttpResponse(html)
