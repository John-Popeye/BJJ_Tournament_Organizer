from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Tournament, Competitor

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class TournamentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Tournament
        fields = ['name', 'date', 'location','tournamentType', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'tournamentType': forms.Select(attrs={'class': 'form-control'}),
            'started': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CompetitorForm(forms.ModelForm):
    class Meta:
        model = Competitor
        fields = ['name', 'age', 'weight', 'belt', 'team', 'tournaments']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'belt': forms.Select(attrs={'class': 'form-control'}),
            'team': forms.TextInput(attrs={'class': 'form-control'}),
            'tournaments': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class AddCompetitorToTournamentForm(forms.Form):
    tournament = forms.ModelChoiceField(queryset=Tournament.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    competitors = forms.ModelMultipleChoiceField(queryset=Competitor.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
