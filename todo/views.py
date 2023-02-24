from django.shortcuts import render
from django.http import HttpResponse
from . models import Todo
# Create your views here.


def home(request):
    todo_list = Todo.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'index.html', context=context)


def create_todo(request):
    return HttpResponse("Create")