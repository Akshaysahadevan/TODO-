from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import ListView
from .froms import TaskForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView


class Tasklistview(ListView):
    models = Task
    templates_name = 'home.html'
    context_objects_name = 'task1'


def home(request):
    task1 = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('task ', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, "home.html", {'task1': task1})


#
# def details(request):

#   return render(request, 'detail.html',)


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, "delete.html")


def update(request,id):
    task = Task.objects.get(id=id)
    f = TaskForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect("/")
    return render(request, "edit.html", {'f': f, 'task': task})
