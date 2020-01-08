from django.shortcuts import render

from .models import Sections, Solutions, Settings

# Create your views here.
def index(request):
    solutions = Solutions.objects.all()
    sections = Sections.objects.all()
    if Settings.objects.filter(key='company_name').count()==0:
        company_name = 'KNOWLEDGE BASE'
    else:
        company_name = Settings.objects.get(key='company_name').value

    context = {'solutions': solutions, 
                'sections': sections,
                'company_name': company_name}

    return render(request, 'main_app/index.html', context)

def by_section(request, section_id):
    pass

def by_process(request, process_id):
    pass

def by_solution(request, process_id):
    pass