from django.shortcuts import render

from .models import Selections, Solutions, Problems

def index(request):
    selections = Selections.objects.all()
    solutions = Solutions.objects.filter()
    context = {'selections': selections, 'solutions': solutions}
    return render(request, 'decision_board/index.html', context)


def by_selection(request, id_selection):
    selections = Selections.objects.all()
    solutions = Solutions.objects.all()
    current_selection = Selections.objects.get(pk=id_selection)
    context = {'selections': selections, 
                'solutions': solutions, 
                'current_selection': current_selection}

    return render(request, 'decision_board/by_selection.html', context)
