from django import forms
from .models import Student

class AddStudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ("first_nm","last_nm","mail","city")
        widgets = {
            'first_nm':forms.TextInput(attrs={'class':'form-control'}),
            'last_nm':forms.TextInput(attrs={'class':'form-control'}),
            'mail':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'})
        }