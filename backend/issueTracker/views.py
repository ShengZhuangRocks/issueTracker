from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Project, Issues
from .forms import CreateIssue, CreateProject
from django.contrib.auth.models import User


# Create your views here.
# class ProjectList(generic.ListView):
#     template_name = 'issueTracker/index.html'
#     context_object_name = 'projects'

#     def get_queryset(self):
#         return  Project.objects.all()


def project_list(request):
    projects = Project.objects.all()
    issues = []

    for project in projects:
        issues_p = project.issues_set.filter(status="1")[:3]
        issues.append(issues_p)
    return render(request, "issueTracker/index_.html", {
        'projects' : projects,
        'issues' : issues
    })


def issues(request, slug):
    project = Project.objects.get(slug = slug)
    return render(request, "issueTracker/issues.html", {'project':project})


@login_required(login_url='accounts:login')
def create_issue(request, slug):
    project = Project.objects.get(slug=slug)
    if request.method == 'POST':
        form = CreateIssue(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('issueTracker:issues', slug=project.slug)
    else:
        form = CreateIssue()
    return render(request, "issueTracker/create_issue.html", {
        'form':form,
        'project':project
        })


def issue(request, slug, pk):
    project = Project.objects.get(slug=slug)
    issue = project.issues_set.get(pk=pk)
    return render(request, "issueTracker/issue.html", {
        "issue":issue,
        'project':project
        })


@login_required(login_url='accounts:login')
def edit(request, slug, pk):
    project = Project.objects.get(slug=slug)
    issue = project.issues_set.get(pk=pk)
    form = CreateIssue(request.POST or None, instance=issue)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('issueTracker:issues', slug=project.slug)
    return render(request, "issueTracker/edit.html", {
        "issue":issue,
        'project':project,
        'form':form
        })


def tasks_assigned_to_me(request):
    projects = Project.objects.all()
    current_user = request.user
    if request.user.is_authenticated:
        issues = Issues.objects.filter(assigned_to=current_user)
        return render(request, "issueTracker/my_tasks_assigned.html", {
            "projects":projects,
            'issues':issues
            })
    return redirect("accounts:login")


def tasks_created_by_me(request):
    projects = Project.objects.all()
    current_user = request.user
    if request.user.is_authenticated:
        issues = Issues.objects.filter(created_by=current_user)
        return render(request, "issueTracker/my_tasks_assigned.html", {
            "projects":projects,
            'issues':issues
            })
    return redirect("accounts:login")

    
