from django.db import models
from .models import Depense, AutreDepense, Realisation, InfosSpecific, Projet

def calculer_total_depenses(projet):
    """Calcule le total des dépenses pour un projet"""
    depense = Depense.objects.filter(id_projet=projet).first()
    if not depense:
        return 0
    
    # Somme des dépenses principales
    total = (
        depense.consommable_divers + 
        depense.salaire_avantages + 
        depense.equipement_materiel
    )
    
    # Ajouter les autres dépenses
    autres_depenses = AutreDepense.objects.filter(depense=depense)
    for autre in autres_depenses:
        total += autre.prix
        
    return total

def calculer_total_realisations(projet):
    """Calcule le total des coûts de réalisation pour un projet"""
    return Realisation.objects.filter(
        id_projet=projet
    ).aggregate(
        total=models.Sum('cout_realisation')
    )['total'] or 0

def verifier_budget(projet):
    """Vérifie la cohérence du budget avec les dépenses et réalisations"""
    infos = InfosSpecific.objects.filter(id_projet=projet).first()
    if not infos or not infos.budget:
        return True, None
        
    total_depenses = calculer_total_depenses(projet)
    total_realisations = calculer_total_realisations(projet)
    total = total_depenses + total_realisations
    
    if total > infos.budget:
        message = (
            f"Le total des dépenses ({total_depenses:,} FCFA) et des réalisations "
            f"({total_realisations:,} FCFA) soit {total:,} FCFA "
            f"dépasse le budget défini ({infos.budget:,} FCFA)"
        )
        return False, message
        
    return True, None