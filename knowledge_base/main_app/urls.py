from django.contrib import admin
from django.urls import path

from .views import index, by_section, by_process, by_problem, ProblemCreateView, SolutionCreateView

urlpatterns = [
    path('', index, name='index'),
    path('section/<int:section_id>/', by_section, name='by_section'),
    path('process/<int:process_id>/', by_process, name='by_process'),
    path('problem/<int:problem_id>/', by_problem, name='by_problem'),
    path('add_problem/', ProblemCreateView.as_view(), name='add_problem'),
    path('add_solution/', SolutionCreateView.as_view(), name='add_solution'),
]