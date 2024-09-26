
from django.shortcuts import render
from django.db.models import Q, F
   # Q is short for query
from django.http import HttpResponse
from store.models import Product

def say_hello(request):
        #keyword = value 
        # gt is for greater than

    #queryset = Product.objects.filter(title__icontains= 'coffee')
        # 'i' before contains is used for solving case sensitive issues.

    queryset = Product.objects.filter(last_update__year=2021)
          
    # queryset = Product.objects.filter(description__isnull= True) 
           #to return all products without description

    queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    #queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
           # it is similar with the above

      # producs: inventory < 10 OR unit_price < 20
    queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20) )
      # it lists all producs either their inventory values are less than 10 or unit_price are less than 20.
      # '|' is an OR operator

       # producs: inventory < 10 OR unit_price < 20
    queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20) )
                    # '~' is a negative form

        # producs: inventory = unit_price 
    queryset = Product.objects.filter(inventory = F('unit_price'))
      # a product having equal inventory and unit_price values

    return render(request, 'hello.html' ,{'name': 'Yonas Muche','products' : list(queryset)})

