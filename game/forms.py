from django import forms

from .models import GameInstance

class NewGameForm(forms.ModelForm):

    class Meta:
        model = GameInstance
        fields = ('title', 'text',)