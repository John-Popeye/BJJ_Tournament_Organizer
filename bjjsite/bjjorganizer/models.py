from django import forms
from django.db import models

from .competitorMatcher import CompetitorMatcher

# Create your models here.

class Tournament(models.Model):
    
    TOURNAMNET_TYPES = [
        ('freeforall', 'Free for All')
    ]
        
    name = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tournamentType = models.CharField(max_length=100,choices=TOURNAMNET_TYPES)
    started = models.BooleanField(default=False)
    
    
    def start_tournament(self):
        competitors = self.competitors.all()
        matcher = CompetitorMatcher()
        match_pairs = matcher.match_competitors(competitors)
        for c1, c2 in match_pairs:
                Match.objects.create(
                    tournament=self,
                    competitor1=c1,
                    competitor2=c2
                )

        self.started = True
        self.save()
        
        
    def is_started(self):
        return self.started

    def __str__(self):
        return self.name

class Competitor(models.Model):
    BELT_CHOICES = [
        ('white', 'White'),
        ('blue', 'Blue'),
        ('purple', 'Purple'),
        ('brown', 'Brown'),
        ('black', 'Black'),
    ]

    
    widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'belt': forms.Select(attrs={'class': 'form-control'}),
            'team': forms.TextInput(attrs={'class': 'form-control'}),
            'tournaments': forms.Select(attrs={'class': 'form-control'}),
        }

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    belt = models.CharField(max_length=10, choices=BELT_CHOICES)
    team = models.CharField(max_length=255)
    tournaments = models.ManyToManyField('Tournament', related_name='competitors', blank=True, null=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='matches', on_delete=models.CASCADE)
    competitor1 = models.ForeignKey(Competitor, related_name='competitor1_matches', on_delete=models.CASCADE)
    competitor2 = models.ForeignKey(Competitor, related_name='competitor2_matches', on_delete=models.CASCADE)
    winner = models.ForeignKey(Competitor, related_name='won_matches', on_delete=models.CASCADE, null=True, blank=True)
    match_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.competitor1} vs {self.competitor2} - {self.tournament.name}"