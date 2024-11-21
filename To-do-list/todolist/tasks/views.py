from django.shortcuts import render, redirect
from .models import Task

def list_tasks(request):
    pending_tasks = Task.objects.filter(status='Pending').order_by('due_date')
    completed_tasks = Task.objects.filter(status='Completed').order_by('due_date')

    return render(request, 'tasks/list_tasks.html', {
        'pending_tasks': pending_tasks, 
        'completed_tasks': completed_tasks
        })

def task_add(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        notes = request.POST.get('notes')
        if task:
            Task.objects.create(task=task, priority=priority, due_date=due_date, notes=notes)
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
        # Fetch updated values from the form
        updated_task = request.POST.get('task', task.task)  # Default to existing value
        priority = request.POST.get('priority', task.priority)
        due_date = request.POST.get('due_date', task.due_date)
        notes = request.POST.get('notes', task.notes)

        # Update the task fields
        task.task = updated_task
        task.priority = priority
        task.due_date = due_date
        task.save()

        return redirect('list_tasks')

    return render(request, 'tasks/task_edit.html', {'task': task})

