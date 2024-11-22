from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import re
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from account.forms import SignUpForm
from projetGestion import settings
from django.template.loader import render_to_string


def index(request):
    return render(request, 'service/index.html')


# function creation
def registerPage(request):
    if request.method != 'POST':
        return render(request, 'account/register.html')
    
    User = get_user_model()
    
    # Récupération des données du formulaire
    username = request.POST.get('username', '').strip()
    email = request.POST.get('email', '').strip()
    password = request.POST.get('password1', '')
    confirmpassword = request.POST.get('password2', '')
    user_type = request.POST.get('user_type')
    
    # Validation des champs...
    
    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # Définir le type d'utilisateur
        if user_type == 'responsable':
            user.is_responsable = True
        elif user_type == 'assistant':
            user.is_assistant = True
        elif user_type == 'charger_programme':
            user.is_charger_programme = True
        elif user_type == 'charger_projet':
            user.is_charger_projet = True
        elif user_type == 'user':
            user.is_user = True
        elif user_type == 'gestion':
            user.is_gestion = True
        
        user.save()

        # Envoyer l'email
        try:
            html_message = render_to_string('account/email_template.html', {
                'username': username,
                'password': password,
                'user_type': user_type
            })
            
            send_mail(
                subject='Création de votre compte',
                message=f'Votre compte a été créé avec succès !\nIdentifiant : {username}\nMot de passe : {password}',
                html_message=html_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Erreur d'envoi d'email : {e}")

        messages.success(request, f"L'utilisateur {username} a été créé avec succès ! Un email avec les identifiants a été envoyé.")
        return redirect('utilisateur')
        
    except Exception as e:
        messages.error(request, f"Une erreur est survenue lors de la création du compte : {str(e)}")
        return redirect('register')

# function connexion
def loginPage(request):
    User = get_user_model()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = re.match(r"^\S+@\S+\.\S+$", username)
        if email:
            user = User.objects.filter(email=username)
            if user.exists():
                username = user.first().username
        user = authenticate(request, username=username, password=password)  
        # Fonction d'authentification
        if user is not None:
            login(request, user)
            # retour a la page d'acceuil
            messages.success(request, 'connexion reussie')
            if user.is_user or user.is_responsable or user.is_assistant or user.is_charger_programme or user.is_charger_projet or user.is_gestion:
                return redirect('dashboard')
            else:
                messages.info(request, "Vous n'etes pas autorise a vous connecter a cette plateforme")
                return redirect('login')
        else:
            messages.warning(request, 'Informations incorrectes')
            return render(request, 'account/login.html')

    return render(request, 'account/login.html')


def logoutUser(request):
    logout(request)
    
    messages.info(request, "Deconnecter avec succes")
    return redirect('login')




