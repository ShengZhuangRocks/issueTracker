from django.shortcuts import render, redirect
from django.views import generic
from .models import Project, Issues
from .forms import CreateIssue, CreateProject

# Create your views here.
class ProjectList(generic.ListView):
    template_name = 'issueTracker/index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return  Project.objects.all()


def issues(request, project_name):
    project = Project.objects.get(project_name = project_name)
    return render(request, "issueTracker/issues.html", {'project':project})


def create(request, project_name):
    # if request.method == 'POST':
    #     form = CreateIssue(request.POST, request.FILES)
    #     if form.is_valid():
    #         instance.save()
    #         return redirect('issueTracker:issues') # not sure redirect take this second arg
    # else:
    project = Project.objects.get(project_name=project_name)
    form = CreateProject()
    return render(request, "issueTracker/create.html", {
        'form':form,
        'project':project
        })


def issue(request, project_name, pk):
    project = Project.objects.get(project_name=project_name)
    issue = project.issues_set.get(pk=pk)
    return render(request, "issueTracker/issue.html", {
        "issue":issue,
        'project':project
        })

# class IssueDetail(generic.DetailView):
#     model = Issues
#     # context_object_name = 'issue'
#     template_name = 'issueTracker/issue.html'

def edit(request, project_name, pk):
    print("primary keeeeeeeeeeeeey", pk)
    project = Project.objects.get(project_name=project_name)
    issue = project.issues_set.get(pk=pk)
    return render(request, "issueTracker/edit.html", {
        "issue":issue,
        'project':project
        })