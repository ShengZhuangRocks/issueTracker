from .models import Issues, Project
from django import forms

class CreateIssue(forms.ModelForm):
    class Meta:
        model = Issues
        fields = [
            'project', 
            'issue_type',
            'title', 
            'description', 
            'created_date',
            'fixed_date',
            'activity',
            'status',
            'created_by',
            'assigned_to',
            'priority',
        ]
        
    
class CreateProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name','project_type','slug']



