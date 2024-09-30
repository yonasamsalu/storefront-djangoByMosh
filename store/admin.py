from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

       # The field that is shown in the admin page
    list_display = ['title', 'unit_price']

       # The list that can be edited
    list_editable = ['unit_price']
       # numbers of lists shown in the admin page
    list_per_page = 10

# Register the Order model with the admin site
admin.site.register(models.Collection)

