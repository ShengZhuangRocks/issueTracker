from django.contrib import admin
from .models import Project, Issues

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_type')

admin.site.register(Project, ProjectAdmin)

class IssuesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'project',
        'issue_type',
        'description',
        'created_date',
        'fixed_date',
        'activity',
        'status',
        'created_by',
        'assigned_to',
        'priority'
    )

admin.site.register(Issues, IssuesAdmin)
