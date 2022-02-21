from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def add(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def edit(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def unknown_path(request, path):
    return HttpResponse("404 error")
