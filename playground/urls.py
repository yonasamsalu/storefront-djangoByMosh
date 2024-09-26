
from django.urls import path
from . import views

urlpatterns=[
    path('hello',views.say_hello, name="helo"),
    path( 'selecting',views.selecting_field, name='select')

]