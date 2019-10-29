from django.shortcuts import render
from django.views import generic
from .models import Project, Issues

# Create your views here.
class ProjectList(generic.ListView):
    template_name = 'issueTracker/index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return  Project.objects.all()


def issues(request, project_name):
    project = Project.objects.get(project_name = project_name)
    return render(request, "issueTracker/issues.html", {'project':project})

def issue(request, project_name, issue_id):
    # make query
    project = Project.objects.get(project_name=project_name)
    issue = project.issues_set.get(pk=issue_id)
    return render(request, "issueTracker/issue.html", {"issue":issue})
