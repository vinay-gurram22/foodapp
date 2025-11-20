from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.


def index(request):
    items = Item.objects.all()
    return render(request,"myapp/index.html",{"items":items})

def detail(request,id):
    item_one =Item.objects.get(id=id)
    return render()
