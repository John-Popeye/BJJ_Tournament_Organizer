from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import AddCompetitorToTournamentForm, CompetitorForm, TournamentForm

from .models import Competitor, Match, Tournament 
from .forms import SignupForm, LoginForm

# Create your views here.
# Home page
def index(request):
    return render(request, 'bjjorganizer/index.html')


# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'bjjorganizer/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'bjjorganizer/login.html', {'form': form})

@login_required(login_url="/app/login/")
def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'bjjorganizer/tournament_list.html', {'tournaments': tournaments})
@login_required(login_url="/app/login/")
def tournament_detail(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    return render(request, 'bjjorganizer/tournament_detail.html', {'tournament': tournament})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url="/app/login/")
def add_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tournament_list')
    else:
        form = TournamentForm()
    return render(request, 'bjjorganizer/add_tournament.html', {'form': form})
@login_required(login_url="/app/login/")
def add_competitor(request):
    if request.method == 'POST':
        form = CompetitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tournament_list')
    else:
        form = CompetitorForm()
    return render(request, 'bjjorganizer/add_competitor.html', {'form': form})

@login_required(login_url="/app/login/")
def start_tournament(request, tournament_id):
    tournament = Tournament.objects.get(pk=tournament_id)
    tournament.start_tournament()
    return redirect('tournament_detail', pk=tournament_id)

@login_required(login_url="/app/login/")
def delete_tournament(request, tournament_id):
    tournament = Tournament.objects.get(pk=tournament_id)
    tournament.delete()
    return redirect('tournament_list')


@login_required(login_url="/app/login/")
def render_bracket(request, tournament_id):
    tournament = Tournament.objects.get(pk=tournament_id)
    print(tournament.tournamentType)
    if tournament.tournamentType == 'freeforall':
        template_name = 'bjjorganizer/free_for_all_bracket.html'
    else:
        # Handle unsupported mode
        pass
    return render(request, template_name, {'tournament': tournament, 'jsontournament': serializers.serialize('json', [tournament])})

@login_required(login_url="/app/login/")
def select_winner(request, match_id):
    if request.method == 'POST':
        match = Match.objects.get(pk=match_id)
        winner_id = request.POST.get('winner')
        if winner_id:
            match.winner_id = winner_id
            match.save()
        return redirect('render_bracket', tournament_id=match.tournament_id)
    return redirect('tournament_list')


@login_required(login_url="/app/login/")
def add_competitor_to_tournament(request):
    if request.method == 'POST':
        form = AddCompetitorToTournamentForm(request.POST)
        if form.is_valid():
            tournament_id = form.cleaned_data['tournament'].id
            print(tournament_id)
            competitor_ids = map(lambda x: x.id, list(form.cleaned_data['competitors']))
            tournament = Tournament.objects.get(pk=tournament_id)
            if tournament.started:
                messages.error(request, 'Tournament has already started')
                return render(request, 'bjjorganizer/add_competitor_to_tournament.html', {'form': form})
            competitors = Competitor.objects.filter(pk__in=competitor_ids)
            tournament.competitors.add(*competitors)
            return redirect('tournament_detail', pk=tournament_id)  # Redirect to tournament detail page
    else:
        form = AddCompetitorToTournamentForm()
    return render(request, 'bjjorganizer/add_competitor_to_tournament.html', {'form': form})

