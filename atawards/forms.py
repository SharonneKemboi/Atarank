from django import forms
from django.db.models import fields
from . models import Project,Profile


class MyProjectForm(forms.ModelForm):
    class Meta:
        model=Project        
        fields=['image',
                 'link',
                 'name',
                 'description',
                 'category',
                 'location',
                 'user',
        ]