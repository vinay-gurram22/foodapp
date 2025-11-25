from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    items = Item.objects.all()
    return render(request,"myapp/index.html",{"items":items})
@login_required
def detail(request,id):
    item_one =Item.objects.get(id=id)
    return render(request,"myapp/detail.html",{"item_one":item_one})
@login_required
def add_item(request):
    form = ItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'myapp/item-form.html',{"form":form,'is_update': False,})
@login_required
def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            return redirect('index')
    return render(request,'myapp/item-form.html',{'form':form,'item': item,'is_update': True,})
@login_required
def delete_item(request,id):
    item_one = Item.objects.get(id=id)
    if request.method == "POST":
        item_one.delete()
        return redirect('index')
    return render(request,'myapp/delete-pop.html',{"item_one":item_one})

