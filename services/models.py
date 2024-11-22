from django.db import models
from account.models import User
import numpy as np

# Create your models here.
class Services(models.Model):
    nom = models.CharField(max_length=300, null=True)
    numero = models.FloatField()

    def __str__(self):
        return self.nom
    
# Projects
class Projet(models.Model):
    nom = models.CharField(max_length=100, null=True)
    created = models.DateField(auto_now_add=True, null=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projets', null=True)

    def __str__(self):
        return self.nom


# Secteur
class Secteur(models.Model):
    titre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.titre
# Sous secteur
class SousSecteur(models.Model):
    titre = models.CharField(max_length=100, null=True)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE, related_name='domaines', null=True)

    def __str__(self):
        return self.titre
    
# Titre Activite
class TitreActivite(models.Model):
    titre = models.CharField(max_length=100, null=True)
    unite_physique = models.CharField(max_length=30, null=True)
    domaine = models.ForeignKey(SousSecteur, on_delete=models.CASCADE, related_name="titre_activite", null=True)

    def __str__(self):
        return self.titre

# Partenaires
class ListPartenaire(models.Model):
    nom = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.nom

# Orientation
class Orientation(models.Model):
    titre = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.titre
    
# Formulaire
class Formulaire(models.Model):
    titre = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.titre
    
# Activite
class Activite(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activites', null=True)
    commune = models.CharField(max_length=50, null=True)
    province = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=50, null=True)
    paroisse = models.CharField(max_length=50, null=True)
    titre = models.CharField(max_length=100, null=True)
    unite_physique = models.CharField(max_length=50, null=True)
    quantite_prevue = models.IntegerField(default=0, null=True)
    cout_realisation = models.IntegerField(default=0, null=True)
    contribution_beneficiaire = models.IntegerField(default=0, null=True)
    contribution_partenaire = models.IntegerField(default=0, null=True)
    total_benef_direct = models.IntegerField(default=0, null=True)
    nbre_benef_direct_homme = models.IntegerField(default=0, null=True)
    nbre_benef_direct_femme = models.IntegerField(default=0, null=True)
    partenaires = models.CharField(max_length=100, null=True)
    id_titre_activites = models.ForeignKey(TitreActivite, on_delete=models.CASCADE, related_name="id_titre_activite", null=True)
    id_secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE, related_name="id_secteur", null=True)
    id_sous_secteur = models.ForeignKey(SousSecteur, on_delete=models.CASCADE, related_name="id_sous_secteur", null=True)
    id_projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="id_projet", null=True)
    planification = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.titre  if self.titre else ''

# Activite
class Realisation(models.Model):
    id_activite = models.ForeignKey(Activite, on_delete=models.CASCADE, related_name='id_activites', null=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='realisations', null=True)
    commune = models.CharField(max_length=50, null=True)
    province = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=50, null=True)
    paroisse = models.CharField(max_length=50, null=True)

    titre = models.CharField(max_length=100, null=True)
    unite_physique = models.CharField(max_length=50, null=True)
    quantite_prevue = models.IntegerField(default=0)
    periode_prevue_debut = models.CharField(max_length=50, null=True)
    periode_prevue_fin = models.CharField(max_length=50, null=True)

    responsable = models.CharField(max_length=50, null=True)
    cout_realisation = models.IntegerField(default=0)
    contribution_beneficiaire = models.IntegerField(default=0)
    contribution_partenaire = models.IntegerField(default=0)
    part_burkina = models.IntegerField(default=0, null=True)
    partenaires = models.CharField(max_length=100, null=True)

    total_benef_direct = models.IntegerField(default=0)
    nbre_benef_direct_homme = models.IntegerField(default=0)
    nbre_benef_direct_femme = models.IntegerField(default=0)

    total_benef_jeune = models.IntegerField(default=0, null=True)
    nbre_benef_jeune_homme = models.IntegerField(default=0, null=True)
    nbre_benef_jeune_femme = models.IntegerField(default=0, null=True)

    id_titre_activites = models.ForeignKey(TitreActivite, on_delete=models.CASCADE, related_name="id_titre_realisation", null=True)
    id_secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE, related_name="id_secteur_plus", null=True)
    id_sous_secteur = models.ForeignKey(SousSecteur, on_delete=models.CASCADE, related_name="id_sous_secteur_plus", null=True)
    id_projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="id_projet_plus", null=True)
    realisation = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.titre
    
# Informations specifique
class InfosSpecific(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projets_specific', null=True)
    nom = models.CharField(max_length=200, null=True)
    date_debut = models.CharField(max_length=50, null=True)
    date_fin = models.CharField(max_length=50, null=True)
    budget = models.IntegerField(default=0, null=True)
    depense_globale = models.IntegerField(default=0, null=True)

    objectifs_principals = models.CharField(max_length=200, null=True)
    benef_direct_homme = models.IntegerField(default=0, null=True)
    benef_direct_femme = models.IntegerField(default=0, null=True)
    total_benef_direct = models.IntegerField(default=0, null=True)
    partenaires = models.CharField(max_length=100, null=True)
    id_projet= models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='id_projet_specific', null=True)
    id_titre_activites = models.ForeignKey(TitreActivite, on_delete=models.CASCADE, related_name="id_titre_activite_specific", null=True)
    id_secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE, related_name="id_secteur_activite_specific", null=True)
    id_sous_secteur = models.ForeignKey(SousSecteur, on_delete=models.CASCADE, related_name="id_sous_secteur_activite_specific", null=True)

    def __str__(self):
        return self.nom if self.nom else "Null"
    
class Resultat(models.Model):
    resultats = models.CharField(max_length=500, null=True)
    id_specific = models.ForeignKey(InfosSpecific, on_delete=models.CASCADE, related_name='id_specific', null=True)

    def __str__(self):
        return self.resultats


# Partenaire
class Partenaire(models.Model):
    nom = models.CharField(max_length=50, null=True)
    part = models.IntegerField(default=0)
    id_activite = models.ForeignKey(Activite, on_delete=models.CASCADE, related_name="id_activite", null=True)
    id_realisation = models.ForeignKey(Realisation, on_delete=models.CASCADE, related_name='id_realisation', null=True)
    id_infos_specifique = models.ForeignKey(InfosSpecific, on_delete=models.CASCADE, related_name='infos_specific', null=True)

    def __str__(self):
        return self.nom
    
class InfosGenerale(models.Model):
    # Informations sur l'organisation
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='generales', null=True)
    id_projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="infos_generale", null=True)
    nom_org = models.CharField(max_length=50, null=True)
    nature_org = models.CharField(max_length=50, null=True)
    sigle = models.CharField(max_length=50, null=True)
    pays_origine = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    province = models.CharField(max_length=100, null=True)
    commune = models.CharField(max_length=100, null=True)
    village = models.CharField(max_length=100, null=True)
    boite_postale = models.CharField(max_length=50, null=True)
    numb_mobile = models.CharField(max_length=50, null=True)
    numb_fixe = models.CharField(max_length=50, null=True)
    adresse_mail = models.CharField(max_length=50, null=True)
    site_web = models.CharField(max_length=50, null=True)
    # Responsable de l'organisation
    nom_complet_resp = models.CharField(max_length=100, null=True)
    nationalite_resp = models.CharField(max_length=50, null=True)
    fonction_resp = models.CharField(max_length=50, null=True)
    numb_fixe_resp = models.CharField(max_length=50, null=True)
    numb_mobile_resp = models.CharField(max_length=50, null=True)
    # Gouvernance interne de l'organisation
    renou_instance = models.CharField(max_length=50, null=True)
    assem_general = models.CharField(max_length=50, null=True)
    session_statut = models.CharField(max_length=50, null=True)
    mandat_bureau = models.CharField(max_length=50, null=True)
    # Repondant pour le canevas
    nom_complet_canevas = models.CharField(max_length=100, null=True)
    numb_fixe_canevas = models.CharField(max_length=50, null=True)
    numb_mobile_canevas = models.CharField(max_length=50, null=True)
    adresse_mail_canevas = models.CharField(max_length=50, null=True)
    # Groupes cibles
    groupes_cibles = models.CharField(max_length=200, null=True)
    autre_groupe = models.CharField(max_length=50, null=True)
    # Nombre du personnel
    total_pers_homme = models.IntegerField(default=0)
    total_pers_femme = models.IntegerField(default=0)
    # Employés nationaux CDI
    em_nation_cdi_homme = models.IntegerField(default=0)
    em_nation_cdi_femme = models.IntegerField(default=0)
    # Employes nationaux CDD
    em_nation_cdd_homme = models.IntegerField(default=0)
    em_nation_cdd_femme = models.IntegerField(default=0)
    # Employés expatriés CDI
    em_expa_cdi_homme = models.IntegerField(default=0)
    em_expa_cdi_femme = models.IntegerField(default=0)
    # Employes expatries CDD
    em_expa_cdd_homme = models.IntegerField(default=0)
    em_expa_cdd_femme = models.IntegerField(default=0)
    # Benevol nation CDI
    benevol_nation_homme = models.IntegerField(default=0)
    benevol_nation_femme = models.IntegerField(default=0)
    # Benevol expa CDD
    benevol_expa_homme = models.IntegerField(default=0)
    benevol_expa_femme = models.IntegerField(default=0)
    # Personnel administration
    personnel_admin_homme = models.IntegerField(default=0)
    personnel_admin_femme = models.IntegerField(default=0)
    # ministeres
    numb_convention = models.CharField(max_length=50, null=True)
    date_debut_minis = models.CharField(max_length=50, null=True)
    date_fin_minis = models.CharField(max_length=50, null=True)
    # Collectivite
    numb_proto_collec = models.CharField(max_length=50, null=True)
    date_debut_collec = models.CharField(max_length=50, null=True)
    date_fin_collec = models.CharField(max_length=50, null=True)
    # Convention
    numb_proto_convent = models.CharField(max_length=50, null=True)
    date_debut_convent = models.CharField(max_length=50, null=True)
    date_fin_convent = models.CharField(max_length=50, null=True)
    groupe_cible_total = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.nom_org
    
class Partenariat(models.Model):
    nom = models.CharField(max_length=50, null=True)
    numero = models.CharField(max_length=100, null=True)
    date_debut = models.CharField(max_length=50, null=True)
    date_fin = models.CharField(max_length=50, null=True)
    id_general = models.ForeignKey(InfosGenerale, on_delete=models.CASCADE, related_name='id_general_part')

    def __str__(self):
        return self.nom
    
class Objectif(models.Model):
    objectifs = models.CharField(max_length=100, null=True)
    id_general = models.ForeignKey(InfosGenerale, on_delete=models.CASCADE, related_name='id_general', null=True)
    id_infos_specifique = models.ForeignKey(InfosSpecific, on_delete=models.CASCADE, related_name='id_specific_infos', null=True)

    def __str__(self):
        return self.objectifs
    
class Situation(models.Model):
    titre = models.CharField(max_length=50, null=True)
    impot = models.IntegerField(default=0)
    cotisation = models.IntegerField(default=0)
    autre_contribution = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    id_projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="situation", null=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='situation_user', null=True)

    def __str__(self):
        return self.titre
    
class Audit(models.Model):
    titre_test = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=100, null=True)
    date_realisation = models.CharField(max_length=50, null=True)
    nom_cabinet = models.CharField(max_length=100, null=True)
    situation = models.ForeignKey(Situation, on_delete=models.CASCADE, related_name='audit_situation')

    def __str__(self):
        return self.titre_test if self.titre_test else 'Titre'
    
class Depense(models.Model):
    id_projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="id_projet_depense", null=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='utilisateur_depense', null=True)
    name = models.CharField(max_length=100)
    consommable_divers = models.IntegerField(default=0)
    salaire_avantages = models.IntegerField(default=0)
    equipement_materiel = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class AutreDepense(models.Model):
    depense = models.ForeignKey(Depense, on_delete=models.CASCADE, related_name='id_autre_depense')
    intitule = models.CharField(max_length=100, null=True)
    prix = models.IntegerField(default=0)

    def __str__(self):
        return self.intitule
    





