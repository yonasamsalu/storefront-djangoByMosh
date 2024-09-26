
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def say_hello(request):
    #keyword = value 
    # gt is for greater than
    queryset = Product.objects.filter(title__icontains= 'coffee')
        # 'i' before contains is used for solving case sensitive issues.

        #queryset = Product.objects.filter(last_update__year=2021)
          
        # queryset = Product.objects.filter(description__isnull= True) to return all products without description

    return render(request, 'hello.html' ,{'name': 'Yonas Muche','products' : list(queryset)})

