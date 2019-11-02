from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=30, primary_key=True)
    Pt = (
        ('DA','destopApp'),
        ('WA','webApp'),
        ('AA','androidApp')
    )
    project_type = models.CharField(max_length=2, choices=Pt)
    slug = models.CharField(max_length=20)

    def __str__(self):
        return self.project_name


class Issues(models.Model):
    # many issues to one project
    # and an issue can only be in one project
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    isst = (
        ('B', 'Bug'),
        ('I', 'Improvement'),
        ('F', 'Feature'),
        ('E', 'Epic')
    )
    issue_type = models.CharField(max_length=1, choices=isst)
    title = models.CharField(max_length=100)  # or summary
    description = models.CharField(max_length=500)
    created_date = models.DateField("date created")
    fixed_date = models.DateField("date fixed", blank=True, null=True)
    activity = models.DateField("last updated date", blank=True, null=True)
    # many to many??, issue can have many status, and a status would have many issue
    # but also status options are limited
    stat = (
        ('1', 'Todo'),
        ('2', 'In progress'),
        ('3', 'In review'),
        ('4', 'Done')
    )
    status = models.CharField(max_length=2, choices=stat)
    # an issue can only have one creator, so still many to one,
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by")
    # an issue can be assigned to one user at a time
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name="assigned_to", blank=True, 
        null=True
        )
    prior = (
        ('1', 'Highest'),
        ('2', 'High'),
        ('3', 'Medium'),
        ('4', 'Lower'),
        ('5', 'Lowest'),
        ('6', 'Done'),
    )
    priority = models.CharField(max_length=2, choices=prior)

    class Meta:
        ordering = ['priority', 'status']

    def __str__(self):
        return self.title





