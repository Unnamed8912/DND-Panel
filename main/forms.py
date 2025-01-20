from .models import character
from django.forms import ModelForm, TextInput

class characterForm(ModelForm):
    class Meta:
        model = character
        fields = ['name','klass','rasa']
        widgets = {
            'name' : TextInput(attrs={
                'placeholder' : 'Введите Имя'
            }),
            'klass' : TextInput(attrs={
                'placeholder' : 'Введите Класс'
            }),
            'rasa' : TextInput(attrs={
                'placeholder' : 'Введите Расу'
            })}
        
class renameForm(ModelForm):
    class Meta:
        model = character
        fields = ['name', 'level','max_health','cur_health', 'klass', 'rasa', 'description']
        widgets = {
            'name' : TextInput(attrs={
                'id' : 'name',
            }),
            'level' : TextInput(attrs={
                'id' : 'level',
            }),
            'max_health' : TextInput(attrs={
                'id' : 'max_health',
            }),
            'cur_health' : TextInput(attrs={
                'id' : 'cur_health',
            }),
            'klass' : TextInput(attrs={
                'id' : 'klass',
            }),
            'rasa' : TextInput(attrs={
                'id' : 'rasa',
            }),
            'description' : TextInput(attrs={
                'id' : 'description',
            })
        }