from django.shortcuts import render, redirect, get_object_or_404

from todos.models import Todo
from todos.forms import TodoForm


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = TodoForm()
    context = {'form': form}
    return render(request, 'todo/create.html', context)


def list_todos(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todo/list.html', context)


def update_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid:
            form.save()
            
            return redirect("list")
    else:
        form = TodoForm(instance=todo)

    return render(request, "todo/update.html", {"form": form})


def delete_todo(request, todo_id):
    poll = get_object_or_404(Todo, pk=todo_id)
    poll.delete()
    return redirect("list")

    
