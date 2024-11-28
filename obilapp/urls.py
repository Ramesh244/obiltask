# core/urls.py
from django.urls import path
from .views import TaskListView, TaskCreateView

urlpatterns = [
    path('tenant/<int:tenant_id>/tasks/', TaskListView.as_view(), name='task_list'),
    path('tenant/<int:tenant_id>/tasks/new/', TaskCreateView.as_view(), name='task_create'),
]
