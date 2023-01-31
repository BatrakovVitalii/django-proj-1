from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from interfaces.models import Coffee

menu = ['Главная страница', 'Статистика']
def order(request):
    coffee = Coffee.objects.all()
    return render(request, "index.html", {'menu': menu,
                                          'title': 'order',
                                          'client': coffee})


