from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Alô mundo. Meu primeiro app Django")
