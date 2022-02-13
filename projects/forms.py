from django.forms import ModelForm
from .models import Project, Review

class projectform(ModelForm):
    class Meta:
        model= Project
        fields= ['title', 'description', 'project_image', 'demo_link', 'source_link', 'tags']



class commentform(ModelForm):
    class Meta:
        model= Review
        fields= ['body', 'value']
    