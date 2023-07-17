from django.shortcuts import render, redirect
from .models import TaskList
from .forms import PostForm 
from .forms import PostForm , UpdateForm
from django.utils import timezone


# Create your views here.
def all_todo(request):
    data = TaskList.objects.all()
    context = {"data": data}
    return render(request, template_name="todo_list/all_todo.html", context=context)

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            TaskList = form.save(commit=False)
            TaskList.author = request.user
            TaskList.start_date = timezone.now()
            TaskList.save()
            return redirect(all_todo)
    else:
        form = PostForm()
    return render(request, 'todo_list/create.html', {'form': form})


def update(request, id):
    data = TaskList.objects.get(id=id)
    form = UpdateForm(instance=data )
    if request.method == "POST":
        data = TaskList.objects.get(id=id)
        form = UpdateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect(all_todo)
    return render(request, 'todo_list/update.html', {'form': form})

def delete(request, id):
    data = TaskList.objects.get(id=id)
    if request.method == "POST":
        data.delete()
        return redirect(all_todo)
    return render(request, 'todo_list/Delete.html', {'item': data})

