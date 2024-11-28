from django.db import models

# Create your models here.

from django.db import models

class Tenant(models.Model):
    """
    Represents a tenant or client in the shared  shema.
    """
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    Represents tasks that are logically isolated per tenate.
    """
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
