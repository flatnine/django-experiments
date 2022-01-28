from django.urls import path
from .views import delete_task, home, tasks, delete_task

urlpatterns = [
    path('', view=home, name='home'),
    path('tasks/', view=tasks, name='tasks'),
    path('tasks/<int:id>/delete/', view=delete_task, name='delete_task'),
]
