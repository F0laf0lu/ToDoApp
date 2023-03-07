from django.shortcuts import get_object_or_404, redirect, render
from . models import Todo
from . forms import TodoForm, SignUpForm
from django.contrib.auth import login
# Create your views here.

def SignUp(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


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
## Issue: Getting todo list specific to a particular user

def update_todo(request, pk):
    item = get_object_or_404(Todo, pk=pk)
    form = TodoForm(instance=item)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/todo')
    return render(request, 'edit.html', {'form': form})


def delete_todo(request, pk):
    item = get_object_or_404(Todo, pk=pk)
    item.delete()
    return redirect('/todo')

