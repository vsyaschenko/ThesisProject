from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Sections, Processes, Problems, Solutions, Settings
from .forms import ProblemForm, SolutionForm

def get_default_context():
    sections = Sections.objects.all()
    
    if Settings.objects.filter(key='company_name').count()==0:
        company_name = 'KNOWLEDGE BASE'
    else:
        company_name = Settings.objects.get(key='company_name').value
    
    return {'sections': sections, 
            'company_name': company_name}

# Create your views here.
def index(request):
    context = get_default_context()
    context['processes'] = Processes.objects.all()

    return render(request, 'main_app/index.html', context)

def by_section(request, section_id):
    context = get_default_context()   
    context['processes'] = Processes.objects.filter(section=section_id)
    context['current_section'] = Sections.objects.get(pk=section_id)

    return render(request, 'main_app/by_section.html', context)

def by_process(request, process_id):
    context = get_default_context()   
    context['problems'] = Problems.objects.filter(process=process_id)
    context['current_process'] = Processes.objects.get(pk=process_id)
    
    return render(request, 'main_app/by_process.html', context)

def by_problem(request, problem_id):
    context = get_default_context()   
    context['current_problem'] = Problems.objects.get(pk=problem_id)
    context['current_solution'] = Solutions.objects.get(problem=problem_id)

    return render(request, 'main_app/by_problem.html', context)

class ProblemCreateView(CreateView):
    template_name = 'main_app/create_problem.html'
    form_class = ProblemForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        default_context = get_default_context()
        context = super().get_context_data(**kwargs)
        context.update(default_context)

        return context

class SolutionCreateView(CreateView):
    template_name = 'main_app/create_solution.html'
    form_class = SolutionForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        default_context = get_default_context()
        context = super().get_context_data(**kwargs)
        context.update(default_context)

        return context        