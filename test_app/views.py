from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

# Create your views here.

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all()
    return render(request, 'test_app/index.html', {'posts':posts,'menu':menu,'title':'Главная страница'})


def about(request):
    return render(request, 'test_app/about.html', {'menu':menu,'title':'О сайте'})


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
