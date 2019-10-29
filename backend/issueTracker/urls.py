from django.urls import path
from . import views

app_name = 'issueTracker'
urlpatterns = [
    path('', views.ProjectList.as_view(), name='project_list'),
    path('<project_name>/', views.issues, name='issues'),
    path('<project_name>/<issue_id>', views.issue, name='issue')
]