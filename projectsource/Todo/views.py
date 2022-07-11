from urllib import response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Tasktable
from .serializers import *

# Create your views here.
@api_view(['GET'])
def index(request):
    content = Tasktable.objects.all()
   
    context = {
        'content':content
    }
    return render(request, 'index.html', context)

def todolist(request):
    content = Tasktable.objects.all()
    context = {
        'content':content
    }
  
    return render(request, 'tasklist.html', context)


def add(request):
    if request.method =='POST':
        title = request.POST.get('title')
        task = request.POST.get('task')
        
        context = Tasktable(
            title = title,
            task =task 
        )
        context.save()
    return redirect('index')


def Edit(request):
    content = Tasktable.objects.all()
    context = {
        'content':content
    }
    return redirect(request, 'index.html' ,context)


def update(request,id):

    if request.method =='POST':
        title = request.POST.get('title')
        task = request.POST.get('task')
        
        context = Tasktable(
            id = id,
            title = title,
            task =task 
        )
        context.save()
    return redirect('index')


def Delete(request,id):
    content= Tasktable.objects.filter(id=id)
    content.delete()
    context = {
        'content':content
    }
    return redirect('index')

