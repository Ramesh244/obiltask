from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tenant, Task

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'tenant', 'completed', 'created_at', 'updated_at')
    list_filter = ('tenant', 'completed')
    search_fields = ('title', 'tenant__name')
