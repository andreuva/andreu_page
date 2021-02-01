from django.shortcuts import render
from django.http import HttpResponse


def demos(request):
    return HttpResponse("<html><body> <h1> DEMOS PAGE </h1> </body></html>")
