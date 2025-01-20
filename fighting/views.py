from django.shortcuts import render, redirect

from main import models
from fighting.models import Journal, Fight, Enemie

def fighting(request):
    if request.method == 'POST':
        if 'deleting-fight-id' in request.POST:
            fight_id = request.POST.get('deleting-fight-id')
            Fight.objects.get(id=fight_id).delete()
        else:
            name = request.POST.get('name-of-fight')
            Fight.objects.create(name=name)

    fights_data = Fight.objects.all().order_by('-id')

    context = {'title' : 'Режим Боя',
               'fights' : fights_data}

    return render(request,'main/fighting.html', context)

def current_fight(request):
    fight_id = request.GET.get('fight_id')
    current_fight = Fight.objects.get(id = fight_id)

    if request.method == 'POST':
        if 'attacker' in request.POST:
            # Запрос на добавление записи в журнал
            attacker = request.POST.get('attacker')
            spell = request.POST.get('spell')
            defender = request.POST.get('defender')
            health = request.POST.get('health')
            Journal.objects.create(attacker=attacker, spell=spell, defender=defender,health=health, id_of_fight = current_fight)
            current_fight.all_damage += int(health)
            current_fight.save()
            current_enemie = Enemie.objects.get(name=defender)
            current_enemie.cur_health -= int(health)
            if current_enemie.cur_health <= 0:
                # Добавить Доп.Запись если кто то умер
                current_enemie.is_dead = True
                current_enemie.cur_health = 0
                Journal.objects.create(attacker=attacker, spell=spell, defender=defender,health=health, id_of_fight = current_fight, is_damage = False)
            current_enemie.save()
        elif 'end_of_fight_id' in request.POST:
            # Закончить текущий бой
            id_of_fight = request.POST.get('end_of_fight_id')
            fight = Fight.objects.get(id=id_of_fight)
            fight.is_ended = True
            fight.save()
            print(id_of_fight)
            return redirect('fighting:fighting')
        elif 'continue_of_fight_id' in request.POST:
            # Возобновить бой
            id_of_fight = request.POST.get('continue_of_fight_id')
            fight = Fight.objects.get(id=id_of_fight)
            fight.is_ended = False
            fight.save()
            print(id_of_fight)
            return redirect('fighting:fighting')
        else:
            # Запрос на добавление врага
            name_enemie = request.POST.get('name_enemie')
            health_enemie = request.POST.get('health_enemie')
            initiative_enemy = request.POST.get('initiative_enemie')
            Enemie.objects.create(name = name_enemie, max_health = health_enemie, cur_health = health_enemie, id_of_fight = current_fight, initiative = initiative_enemy)
    
    characters_data = models.character.objects.all().order_by('-initiative')

    enemies_data = Enemie.objects.all().filter(id_of_fight = current_fight).order_by('-initiative')
    journal_data = Journal.objects.all().filter(id_of_fight = current_fight).order_by('-id')


    context = {'title' : 'Бой',
               'characters' : characters_data,
               'enemies' : enemies_data,
               'fight' : current_fight,
               'journals' : journal_data,}
    return render(request, 'main/current_fight.html', context)