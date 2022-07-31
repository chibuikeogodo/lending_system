from django import forms
from .models import TimeTable

class ExamForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = '__all__'
        widgets = {
            'course_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'course_title'}),
            'course_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'course_code'}),
            'hall': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'hall'}),
            'time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'time'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'department'}),
            'invigilators': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'invigilators'}),


        }
