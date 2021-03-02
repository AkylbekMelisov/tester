from django import forms
from .models import *


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
