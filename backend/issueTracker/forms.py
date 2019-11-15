from .models import Issues, Project
from django import forms

class CreateIssue(forms.ModelForm):
    class Meta:
        model = Issues
        fields = (
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
        )

        # widgets = {
        #     'created_date': forms.DateTimeInput(attrs={
        #         'class': 'form-control datetimepicker-input',
        #         'data-target': '#datetimepicker1'
        #     }),
        #     'fixed_date': forms.DateTimeInput(attrs={
        #         'class': 'form-control datetimepicker-input',
        #         'data-target': '#datetimepicker2'
        #     }),
        #     'activity': forms.DateTimeInput(attrs={
        #         'class': 'form-control datetimepicker-input',
        #         'data-target': '#datetimepicker3'
        #     }),
        # }

        # input_formats={
        #     'created_date': ['%d/%m/%Y %#I:%M %p'],
        #     'fixed_date': ['%d/%m/%Y %#I:%M %p'],
        #     'activity': ['%d/%m/%Y %#I:%M %p'],
        # }
        
    
class CreateProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name','project_type','slug']



