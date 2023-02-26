from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from . models import Todo
from . forms import TodoForm
# Create your views here.


def home(request):
    todo_list = Todo.objects.all()
    if request.method == 'GET':
        form = TodoForm()
    elif request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo')
    return render(request, 'index.html', {'todo_list':todo_list, 'form':form})



def delete_todo(request, pk):
    item = get_object_or_404(Todo, pk=pk)
    item.delete()
    return redirect('/todo')

