from django.contrib import admin
from .models import Project, Issues

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_type', 'slug')

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

    # def save_model(self, request, instance, form):
    #     user = request.user
    #     instance = form.save(commit=False)
    #     if not instance.created_by:
    #         instance.created_by=user
    #     instance.save()
    #     return instance

    # def save_model(self, request, obj, form, change):
    #     obj.created_by = request.user
    #     super(IssuesAdmin, self).save_model(request, obj, form, change)
        

admin.site.register(Issues, IssuesAdmin)

