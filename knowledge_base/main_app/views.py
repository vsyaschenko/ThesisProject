from django.shortcuts import render

# Create your views here.
def index(request):
    
    context = {}
    return render(request, 'main_app/index.html', context)

def by_section(request, section_id):
    pass

def by_process(request, process_id):
    pass