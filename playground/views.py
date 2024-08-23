
from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    context= {'name':'Yonas'}
    return render(request, 'hello.html',context)

