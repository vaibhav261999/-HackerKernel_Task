from django import forms
from .models import User, Task

class User_Form(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

    def clean_Email(self):
        email=self.cleaned_data['Email']
        
        if len(email)<15 and "@" in email:
            raise forms.ValidationError('Email must be eaual or grater then 15 charactors')
        return email

class Task_form(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'