from django.urls import path, re_path
from . import views

app_name = 'issueTracker'

urlpatterns = [
    path('', views.project_list, name='projects_list'),
    path('<slug:slug>/issues/', views.issues, name='issues'),
    path('<slug:slug>/create-issue/', views.create_issue, name='create_issue'),
    path('<slug:slug>/issue/<int:pk>/', views.issue, name='issue'),
    path('<slug:slug>/edit/<int:pk>/', views.edit, name='edit'),
    path('my-tasks_assigned/', views.tasks_assigned_to_me, name='my_tasks_assigned'),
    path('my-tasks_created/', views.tasks_created_by_me, name='my_tasks_created'),
]