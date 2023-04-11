from django.shortcuts import render,get_object_or_404
from .models import *






def clients(request):
    client=Client.objects.all
    return render(request,"new/clients.html",{"client":client})


def izdelie_list(request):
    izdelia = Izdelie.objects.all()
    return render(request, 'new/izdelie_list.html', {'izdelia': izdelia})


def izdelie_detail(request, pk):
    izdelie = get_object_or_404(Izdelie, pk=pk)
    products = Products.objects.filter(izdelie=izdelie)
    return render(request, 'new/izdelie_detail.html', {'izdelie': izdelie, 'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'new/product_detail.html', {'product': product})
