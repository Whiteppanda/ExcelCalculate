from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.


def index(request):
    todos = ToDo.objects.all()
    content = {'todos': todos}
    return render(request, 'index.html', content)


def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = ToDo(content=user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))


def doneTodo(request):
    user_input_id = request.GET['todoNum']
    todo = ToDo.objects.get(id=user_input_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))
