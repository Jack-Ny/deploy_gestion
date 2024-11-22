from django import forms

class ChangePasswordForm(forms.Form):
    ancien_mdp = forms.CharField(label='Ancien mot de passe', widget=forms.PasswordInput)
    nouveau_mdp = forms.CharField(label='Nouveau mot de passe', widget=forms.PasswordInput)
    confirm_nouveau_mdp = forms.CharField(label='Confirmer le nouveau mot de passe', widget=forms.PasswordInput)