from django.shortcuts import render

from fighting.models import Fight, Journal

def history(request):
    fight_data = Fight.objects.all()

    context = {'title' : 'История',
               'fights' : fight_data,
    }

    return render(request, 'main/history.html', context)

def review(request):
    fight_id = request.GET.get('fight_id')
    current_fight = Fight.objects.get(id=fight_id)

    journal_data = Journal.objects.all().filter(id_of_fight = current_fight).order_by('-id')

    context = {
        'title' : 'Обзор',
        'journals' : journal_data
    }
    return render(request,'main/review.html', context)