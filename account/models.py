from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('Est un administrateur', default=False)
    is_responsable = models.BooleanField('Est un responsable de suivi', default=False)
    is_assistant = models.BooleanField('Est un assistant', default=False)
    is_charger_programme = models.BooleanField('Est un chargé de programme', default=False)
    is_charger_projet = models.BooleanField('Est un chargé de projet', default=False)
    is_user = models.BooleanField('Est un utilisateur', default=False)
    is_gestion = models.BooleanField('Est un gestionnaire', default=False)

    @property
    def user_type_defined(self):
        # Vérifie si au moins un des champs is_* est True
        return any([self.is_admin, self.is_responsable, self.is_assistant, 
                    self.is_charger_programme, self.is_charger_projet, self.is_user, self.is_gestion])
