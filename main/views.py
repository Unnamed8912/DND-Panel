from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.models import character
from main.forms import characterForm, renameForm

def characters(request):
    charactersdata = character.objects.all()
    
    context = {
        'title' : 'Персонажи',
        'characters' : charactersdata,
    }
    return render(request, 'main/characters.html', context)

def display_character(request, slug):
    if request.method == 'POST':
        character_id = request.POST.get('character_id')
        character.objects.get(id=character_id).delete()
        return redirect('main:characters')
    
    character_d = character.objects.get(slug=slug)
    
    charactersdata = character.objects.all()

    context = {
        'title' : 'Персонажи',
        'characters' : charactersdata,
        'character_d' : character_d
    }
    
    return render(request, 'main/display.html', context)

def rename_character(request, slug):
    character_d = character.objects.get(slug=slug)

    charactersdata = character.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        level = request.POST.get('level',15)
        max_health = request.POST.get('max_health',10)
        cur_health = request.POST.get('cur_health',10)
        klass = request.POST.get('klass')
        rasa = request.POST.get('rasa')
        description = request.POST.get('description')
        character_d.name = name
        character_d.level = level
        character_d.max_health = max_health
        character_d.cur_health = cur_health
        character_d.klass = klass
        character_d.rasa = rasa
        character_d.description = description
        character_d.save()
        return redirect('main:characters')

    form = renameForm()

    context = {
        'title' : 'Редактирование',
        'character_d' : character_d,
        'characters' : charactersdata,
        'form' : form
    }

    return render(request, 'main/rename.html', context)

def create(request):
    if request.method == 'POST':
        form = characterForm(request.POST)
        if form.is_valid():
            form.save()

    charactersdata = character.objects.all()
    
    form = characterForm()
    
    context = {
        'title' : 'Создать Персонажа',
        'characters' : charactersdata,
        'form' : form,
    }
    return render(request, 'main/create.html', context)

def home(request):
    return render(request,'main/home.html')