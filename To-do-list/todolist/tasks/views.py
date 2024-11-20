from django.shortcuts import render, redirect
from .models import Task

def list_tasks(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list_tasks.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        priority = request.POST.get('priority')
        if task:
            Task.objects.create(task=task, priority=priority)
        return redirect('list_tasks')

def task_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = 'Completed'
    task.save()
    return redirect('list_tasks')

def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('list_tasks')

def task_edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.tasks = request.POST['tasks']
        task.description = request.POST['description']
        task.save()
        return redirect('list_tasks')
    return render(request, 'tasks/task_edit.html', {'task': task})

