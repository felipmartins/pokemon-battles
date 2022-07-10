from random import random
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import random_pokemon_team_generator, index, new_user, generate_pokemon_team

urlpatterns = [
    path('', index, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='auth-login'),
    path("logout/", auth_views.LogoutView.as_view(template_name="login.html"), name="auth-logout",),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("new-user/", new_user, name="new-user"),
    path('pokemon_team_api', random_pokemon_team_generator, name='api'),
    path('generate_team/<int:user_id>', generate_pokemon_team, name='generate-team'),
]
