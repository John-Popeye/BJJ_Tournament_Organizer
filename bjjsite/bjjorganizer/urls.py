from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('tournaments/', views.tournament_list, name='tournament_list'),
    path('tournaments/<int:pk>/', views.tournament_detail, name='tournament_detail'),
    path('tournaments/add/', views.add_tournament, name='add_tournament'),
    path('competitors/add/', views.add_competitor, name='add_competitor'),
    path('tournaments/<int:tournament_id>/start/', views.start_tournament, name='start_tournament'),
    path('tournaments/<int:tournament_id>/delete/', views.delete_tournament, name='delete_tournament'),
    path('tournaments/<int:tournament_id>/bracket/', views.render_bracket, name='render_bracket'),
    path('match/<int:match_id>/select_winner/', views.select_winner, name='select_winner'),
    path('add_competitor_to_tournament/', views.add_competitor_to_tournament, name='add_competitor_to_tournament'),


]