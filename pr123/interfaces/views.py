from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def order(request):
    lst = [{"id": 1, "name": "Andrew", "coffee": "Raf"},
           {"id": 2, "name": "Victor", "coffee": "Latte"}]
    order = {"order": lst}
    return render(request, "index.html", context=order)


