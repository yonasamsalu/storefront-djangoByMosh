from django.contrib import admin
from . import models

# @admin.register(models.Product)
# class ProductAdmin(admin.ModelAdmin):

#        # The field that is shown in the admin page
#     list_display = ['title', 'unit_price']

#        # The list that can be edited
#     list_editable = ['unit_price']
#        # numbers of lists shown in the admin page
#     list_per_page = 10

# # Register the Order model with the admin site
# admin.site.register(models.Collection)

@admin.register(models.Product)
class CustomerAdmin(admin.ModelAdmin):
   #  list_display = ['first_name', 'last_name', 'membership', 'inventory']
   #  list_editable = ['membership']
   #  ordering = ['first_name', 'last_name']
   #  list_per_page = 10


    list_display = ['title', 'unit_price', 'inventory_status']
    list_editable = ['unit_price']
    list_per_page = 10
    
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory <10:
            return 'low'
        return 'ok'
            


