from django.shortcuts import render

def index(request):
    return render(request, "index.html",
                  {'title': 'Главная'})
def contacts(request):
    return render(request, "contacts.html",
                  {'title': 'Контакты'})
def catalog(request):
    return render(request, "catalog.html",
                  {'title': 'Каталог'})
def corf(request):
    return render(request, "corf.html",
                  {'title': 'Корзина'})