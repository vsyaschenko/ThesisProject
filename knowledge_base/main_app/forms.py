from django.forms import ModelForm

from .models import Problems, Solutions

class ProblemForm(ModelForm):
    class Meta:
        model = Problems
        fields = ('process', 'name', 'content', 'relevant')

class SolutionForm(ModelForm):
    class Meta:
        model = Solutions
        fields = ('problem', 'content', 'relevant')