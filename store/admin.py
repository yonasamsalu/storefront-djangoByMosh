from django.contrib import admin
from . import models


# Register the Order model with the admin site
admin.site.register(models.Collection)
admin.site.register(models.Product)
