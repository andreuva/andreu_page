from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return HttpResponse("<html><body> <h1> PROJECTS PAGE </h1> </body></html>")
