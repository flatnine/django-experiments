from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Task

def home(request):
    return HttpResponse("Tasks list")


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'display_tasks.html', {'tasks': tasks})

@require_http_methods(['DELETE'])
def delete_task(request, id):
    Task.objects.filter(id=id).delete()
    tasks = Task.objects.all()
    return render(request, 'tasks_lists.html', {'tasks': tasks})