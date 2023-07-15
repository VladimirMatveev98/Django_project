from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.

def index(request):
    return HttpResponse("Страница первого тестового приложения")


def categories(request, someID):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Заголовок первого уровня</h1><p>{someID}</p>")


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
