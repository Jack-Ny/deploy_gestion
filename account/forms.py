from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User



class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=90)
    
    class meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user