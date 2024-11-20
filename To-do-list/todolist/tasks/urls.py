from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_tasks, name='list_tasks'),
    path('add/', views.task_add, name='task_add'),
    path('task_complete/<task_id>', views.task_complete, name='task_complete'),
    path('task_delete/<task_id>', views.task_delete, name='task_delete'),
    path('task_edit/<task_id>', views.task_edit, name='task_edit'),
]