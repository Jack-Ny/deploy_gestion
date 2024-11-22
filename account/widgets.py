from django.forms import TextInput, EmailInput, PasswordInput
from django.utils.translation import gettext as _

class CustomUsernameInput(TextInput):
    def __init__(self, attrs=None):
        if not attrs:
            attrs = {}
        attrs['class'] = 'form-control form-control-user'
        attrs['placeholder'] = _('Nom d\'utilisateur')
        super().__init__(attrs=attrs)

class CustomEmailInput(EmailInput):
    def __init__(self, attrs=None):
        if not attrs:
            attrs = {}
        attrs['class'] = 'form-control form-control-user'
        attrs['placeholder'] = _('Adresse mail')
        super().__init__(attrs=attrs)


class CustomPasswordInput(PasswordInput):
    def __init__(self, attrs=None):
        if not attrs:
            attrs = {}
        attrs['class'] = 'form-control form-control-user'
        attrs['placeholder'] = _('Mot de passe')
        super().__init__(attrs=attrs)

class CustomRepeatPasswordInput(PasswordInput):
    def __init__(self, attrs=None):
        if not attrs:
            attrs = {}
        attrs['class'] = 'form-control form-control-user'
        attrs['placeholder'] = _('Répéter le mot de passe')
        super().__init__(attrs=attrs)
