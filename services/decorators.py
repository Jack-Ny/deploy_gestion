from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.urls import reverse_lazy
from account.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages

# recuperer le modele de l'utilisation
User = get_user_model()


# Donner les accces a tout les utilisateurs
def all_user_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type_defined:
            # si l'utilisateur est authentifier et a un type definie
            return view_func(request, *args, **kwargs)
        
        messages.info(request, 'Vous ne pouvez pas accéder à cette page')
        return redirect('index')
    return _wrapped_view

# Donner les accces au reponsable
def responsable_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_responsable:
            # si l'utilisateur est authentifier et est de type responsable il accede a la vue
            return view_func(request, *args, **kwargs)
            
        # Si l'utilisateur n'est pas authentifié ou n'est pas de type 'responsable'
        messages.info(request, 'Vous ne pouvez pas accéder à cette page')
        return redirect('index')
    
    return _wrapped_view


# Donner les accces au reponsable et au charger du programme
def responsable_charger_projet_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and (request.user.is_responsable or request.user.is_charger_projet) and request.user.user_type_defined:
            # si l'utilisateur est authentifier et est soit responsable soit charger du projet
            return view_func(request, *args, **kwargs)
        
        # si ce n'est pas le cas
        messages.info(request, 'Vous ne pouvez pas accéder à cette page')
        return redirect('index')
    
    return _wrapped_view
