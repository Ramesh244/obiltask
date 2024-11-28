from django.shortcuts import render

# Create your views here.
# core/views.py
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Tenant, Task

class TaskListView(ListView):
    """
    Displays tasks for a specific tenant.
    """
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        tenant_id = self.kwargs['tenant_id']
        return Task.objects.filter(tenant_id=tenant_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tenant_id = self.kwargs['tenant_id']
        context['tenant'] = get_object_or_404(Tenant, id=tenant_id)
        return context


class TaskCreateView(CreateView):
    """
    Allows creating a new task for a specific tenant.
    """
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'task_form.html'

    def form_valid(self, form):
        tenant_id = self.kwargs['tenant_id']
        tenant = get_object_or_404(Tenant, id=tenant_id)
        form.instance.tenant = tenant
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tenant_id = self.kwargs['tenant_id']
        context['tenant'] = get_object_or_404(Tenant, id=tenant_id)
        return context


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class TestRateLimitView(APIView):
    """
    An API endpoint with rate limiting applied.
    """
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request, *args, **kwargs):
        return Response({'message': 'This is a rate-limited endpoint!'})
