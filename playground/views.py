
from django.shortcuts import render
from django.db.models import Q, F
from django.db.models import Value, Func, Count
from django.db.models import DecimalField, ExpressionWrapper
from django.contrib.contenttypes.models import ContentType
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg
from django.db import transaction, connection

   # Q is short for query
from django.http import HttpResponse
from store.models import Product, OrderItem, Order,Customer, Collection
from tags.models import TaggedItem 

# def say_hello(request):
        #keyword = value 
        # gt is for greater than

    #queryset = Product.objects.filter(title__icontains= 'coffee')
        # 'i' before contains is used for solving case sensitive issues.

    # queryset = Product.objects.filter(last_update__year=2021)
          
    # # queryset = Product.objects.filter(description__isnull= True) 
    #        #to return all products without description

    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    #        # it is similar with the above

    #   # producs: inventory < 10 OR unit_price < 20
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20) )
    #   # it lists all producs either their inventory values are less than 10 or unit_price are less than 20.
    #   # '|' is an OR operator

    #    # producs: inventory < 10 OR unit_price < 20
    # queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20) )
    #                 # '~' is a negative form

    #     # producs: inventory = unit_price 
    # queryset = Product.objects.filter(inventory = F('unit_price'))
    #   # a product having equal inventory and unit_price values

    # queryset = Product.objects.order_by('title')
    #   # sort products by ascending order

    # queryset = Product.objects.order_by('unit_price' ,'-title')
    #     # unit_price in ascending order and title in descending order

    # queryset = Product.objects.order_by('unit_price' ,'-title').reverse()
    #        # reverse the directions of the sort


    
    # return render(request, 'hello.html' ,{'name': 'Yonas Muche','products' : list(queryset)})


    # product = Product.objects.order_by('unit_price')[0]
      # to return an individual field


   # return render(request, 'hello.html' ,{'name': 'Yonas Muche','product' : 'product'})


      # to return the first five objects in the arrey, 0,1,2,3,4 exclude five
#     queryset = Product.objects.all()[:5]

#            # seleting fields in query
#     queryset = Product.objects.values('id', 'title', 'collection__title')

     

#     return render(request, 'hello.html' ,{'name': 'Yonas Muche','products' : list(queryset)})

# def selecting_field(request):
#    #  sets = Product.objects.values('id', 'title', 'collection__title')
#    #      # we get the result in dictionary form

#    #  sets = Product.objects.values_list('id', 'title', 'collection__title')
#    #      # we get the result in tuple form and the values only


#    #  sets = Product.objects.order_by('title')

#    #  context = {'productions' : list(sets)}


#    #  return render(request, 'hello2.html' , context)



#    #  queryset = OrderItem.objects.values('product_id').distinct()
#    #  context = {'productions' : list(product)}

#     product = Product.objects.filter(id__in = OrderItem.objects.values('product_id').distinct())  
   

#        # we use distinct() method to remove diplication
#     product = Product.objects.filter(id__in = OrderItem.objects.values('product_id').distinct()).order_by('title')   

#          # To specify the field that we wanna read from the db    
#     product = Product.objects.only('id', 'title')

#     product = Product.objects.defer('description')


#     context = {'productions' : list(product)}


#     return render(request, 'hello2.html' , context)


# def seleting_releted_field(request):
#     # select_related (1)
#     # prefetch_related (n)   
#     queryset2 = Product.objects.select_related('collection').all()
#     queryset2 = Product.objects.prefetch_related('promotions').select_related('collection').all()

#       # Get the last 5 orders with their customer and items (inlude product) 
#     queryset3 = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at') [:5]


# def aggrigate(request):
#             # Aggregating Objects
#     result = Product.objects.aggregate(count= Count('id'), min_price = Min('unit_price'))

#          # Annotating Objects
#     result = Customer.objects.annotate(new_id=F('id'))

#          # CONCAT
#     result = Customer.objects.annotate(full_name=Func(F('first_name'),Value(''),F('last_name'), function='CONCAT'))
    
#     result = Customer.objects.annotate(full_name=Concat('first_name', Value(''), 'last_name'))


#     queryset = Customer.objects.annotate(orders_count=Count('order'))


#     discounted_price=ExpressionWrapper(F('unit_price') * 0.8 , output_field=DecimalField())
#     queryset = Product.objects.annotate(discounted_price = discounted_price)


#     context = {'name':'Yonas','result': list(queryset)}


#     return render(request, 'hello4.html', context)

def say_hello(request):
    
    # TaggedItem.objects.get_tags_for(Product, 1)

    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects.select_related('tag').filter(content_type=content_type, id=1)

    #         # queryset cache
    # queryset = Product.objects.all()
    # list(queryset)
    # queryset[0]

    #      # creating objects
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product=Product(pk=1)
    # collection.save()
    # collection.id

    #       # updating objects
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product=None
    # collection.save()

    #  # to update the whole objects from the Collection table
    # Collection.objects.update(featured_product=None)
        
    #     # to update a single object
    # Collection.objects.filter(pk=11).update(featured_product=None)

    #      # Deleting multiple objects 
    #      # in this case all objects their id is grearer than five
    # Collection.objects.filter(id__range=(11,16)).delete()

    #     # Deleting a single object
    # collection=Collection.objects(pk = 11)
    # collection.delete()

    # ...

    # with transaction.atomic():
    #     order =Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()

    #     # Select all fields from store_product table
    # queryset = Product.objects.raw('SELECT * FROM store_product')

    #      # Select id and title fields from the table
    # queryset = Product.objects.raw('SELECT id, title FROM store_product')


          # we can delete update and so on in the excute() method
    

    context = {'name':'Yonas'}

    return render(request,'hello.html',context)