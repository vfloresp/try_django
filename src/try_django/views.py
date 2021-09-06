from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, "hello_world.html")


def about_page(request):
    return HttpResponse('<h1>About us</h1>')


def contact_page(request):
    return HttpResponse('<h1>Conact us</h1>')
