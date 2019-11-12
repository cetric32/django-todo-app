from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Todo

# Create your views here.


def home(request):
    return render(request,'todo/home.htm')

def todo_list(request):
    todos = Todo.objects.all()
    context = {'todos': todos}

    return render(request,'todo/todo_list.htm',context)

def todo_item(request,todo_id):
    todo_item = get_object_or_404(Todo,id=todo_id)
    context = {'todo_item':todo_item}
    return render(request,'todo/todo_item.htm',context)
