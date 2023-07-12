from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Страница первого тестового приложения")


def categories(request):
    return HttpResponse("<h1>Заголовок первого уровня<h1>")
