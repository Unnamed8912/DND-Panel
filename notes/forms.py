from .models import Notes
from django.forms import ModelForm, TextInput

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields =['textData']

        widgets = {
            'textData' : TextInput(attrs={
                'class' : 'form-place',
                'placeholder' : 'Введите заметку',
            })
        }