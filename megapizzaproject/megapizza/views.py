from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages

def kitchen(request):
    orders = OrderInfo.objects.all()
    return render(request, 'kitchen.html', {'orders': orders})

def index(request):
    return render(request, "index.html",
                  {'title': 'Главная -'})
def contacts(request):
    return render(request, "contacts.html",
                  {'title': 'Контакты -'})
def catalog(request):
    return render(request, "catalog.html",
                  {'title': 'Каталог -'})
def corf(request):
    return render(request, "corf.html",
                  {'title': 'Корзина -'})
def pers_cab(request):
    return render(request, "pers_cab.html",
                  {'title': 'Личный кабинет -'})
def kitchen(request):
    return render(request, "kitchen.html",
                  {'title': 'Стол заказов -'})

def new(request):
    return render(request, "new.html",
                  {'title': 'Стол заказов -'})

class SignUp(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreatForm
    success_url = reverse_lazy("login")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Вы успешно зарегистрировались!')
        return response

def orders(request):
    return render(request, "main/profile_orders.html", {
        'tovars': kitchen.objects.all(), 
        'orders': kitchen.objects.filter(user = request.user),
    })
