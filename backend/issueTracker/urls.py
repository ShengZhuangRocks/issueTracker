from django.urls import path, re_path
from . import views

app_name = 'issueTracker'

urlpatterns = [
    path('', views.ProjectList.as_view(), name='projects'),
    path('<project_name>/issues/', views.issues, name='issues'),
    re_path(r'<project_name>/create/$', views.create, name='create_new'),
    path('<project_name>/issue/<int:pk>/', views.issue, name='issue'),
    path('<project_name>/edit/<int:pk>/', views.edit, name='edit'),
]