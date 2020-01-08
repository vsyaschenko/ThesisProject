from django.shortcuts import render

from .models import Sections, Solutions

# Create your views here.
def index(request):
    solutions = Solutions.objects.all()
    sections = Sections.objects.all()
    context = {'solutions': solutions, 'sections': sections}

    return render(request, 'main_app/index.html', context)

def by_section(request, section_id):
    pass

def by_process(request, process_id):
    pass

def by_solution(request, process_id):
    pass