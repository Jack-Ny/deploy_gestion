from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('api/partenaires/', views.get_partenaires, name='get_partenaires'),
    path('selection/', views.selection, name='selection'),
    path('synthese_par_projet/', views.synthese_par_projet, name='synthese_par_projet'),
    path('telecharger_<str:format>/', views.generer_synthese, name='telecharger_synthese'),
    path('synthese_globale_requis/', views.synthese_globale_requis, name='synthese_globale_requis'),
    path('pdf_generale_invoice/', views.generate_pdf, name='pdf_generale_invoice'),
    path('generate_word/', views.generate_word, name='generate_word'),
    path('generate_excel/', views.generate_excel, name='generate_excel'),

    path('parametres/', views.parametres, name='parametres'),
    path('utilisateur/', views.utilisateur, name='utilisateur'),
    path('utilisateur/modifier_utilisateur', views.modifier_utilisateur, name='modifier_utilisateur'),
    path('get-domaines/', views.get_domaines, name='get_domaines'),
    path('get-activites/', views.get_activites, name='get_activites'),
    path('get_activite_details/', views.get_activite_details, name='get_activite_details'),
    path('get_activite/', views.get_activite, name='get_activite'),
    
    path('documentation/', views.documentation, name="documentation"),
    path('return_pdf/', views.return_pdf, name='return_pdf'),

    path('', views.index, name='index'),
    path('profil/', views.profils, name='profils'),
    path('change_password/', views.change_password, name='change_password'),
    path('service/', views.service, name='service'),

    path('generate_pdf_situation/', views.generate_pdf_situation, name='generate_pdf_situation'),
    path('generate_word_situation/', views.generate_word_situation, name='generate_word_situation'),
    path('generate_excel_situation/', views.generate_excel_situation, name='generate_excel_situation'),

    path('generate_pdf_generale/', views.generate_pdf_generale, name='generate_pdf_generale'),
    path('generate_excel_generale', views.generate_excel_generale, name='generate_excel_generale'),
    path('generate_word_generale', views.generate_word_generale, name='generate_word_generale'),

    path('generate_pdf_planification/', views.generate_pdf_planification, name='generate_pdf_planification'),
    path('generate_word_planification/', views.generate_word_planification, name='generate_word_planification'),
    path('generate_excel_planification/', views.generate_excel_planification, name='generate_excel_planification'),

    path('generate_pdf_suivi/', views.generate_pdf_suivi, name='generate_pdf_suivi'),
    path('generate_word_suivi/', views.generate_word_suivi, name='generate_word_suivi'),
    path('generate_excel_suivi/', views.generate_excel_suivi, name='generate_excel_suivi'),

    path('generate_pdf_depense/', views.generate_pdf_depense, name='generate_pdf_depense'),
    path('generate_word_depense/', views.generate_word_depense, name='generate_word_depense'),
    path('generate_excel_depense/', views.generate_excel_depense, name='generate_excel_depense'),

    path('generate_pdf_specifique/', views.generate_pdf_specifique, name='generate_pdf_specifique'),
    path('generate_word_specifique/', views.generate_word_specifique, name='generate_word_specifique'),
    path('generate_excel_specifique/', views.generate_excel_specifique, name='generate_excel_specifique'),

    path('generate_pdf_globale/', views.generate_pdf_globale, name='generate_pdf_globale'),
    path('generate_word_globale/', views.generate_word_globale, name='generate_word_globale'),
    path('generate_excel_globale/', views.generate_excel_globale, name='generate_excel_globale'),

    path('synthese_generale/', views.globale_generale, name='globale_generale'),
    path('synthese_situation/', views.globale_situation, name='globale_situation'),
    path('synthese_planification/', views.globale_planification, name='globale_planification'),
    path('synthese_suivi/', views.globale_suivi, name='globale_suivi'),
    path('synthese_depense/', views.globale_depense, name='globale_depense'),
    path('synthese_specifique/', views.globale_specifique, name='globale_specifique'),
    path('synthese_globale/', views.globale_globale, name='globale_globale'),

    path('create_projet/', views.create_projet, name='create_projet'),

    path('projet/<int:projet_id>/choix_form/infos_specifique/', views.infos_specifique, name='infos_specifique'),
    path('projet/<int:projet_id>/choix_form/infos_specifique/ajouter_infos_specifique', views.ajouter_infos_specifique, name='ajouter_infos_specifique'),
    path('projet/<int:projet_id>/choix_form/infos_specifique/modifier_infos_specifique/<int:specific_id>/', views.modifier_infos_specifique, name='modifier_infos_specifique'),
    path('projet/<int:projet_id>/choix_form/infos_specifique/view_infos_specifique<int:specific_id>/', views.view_infos_specifique, name='view_infos_specifique'),
    # path('infos_specifique/ajouter_infos_specifique/', views.ajouter_infos_specifique, name='ajouter_infos_specifique'),
    # path('modifier_infos_specifique/', views.modifier_infos_specifique, name='modifier_infos_specifique'),
    # path('view_infos_specifique/', views.view_infos_specifique, name='view_infos_specifique'),

    path('projet/', views.projet, name='projet'),
    path('projet/<int:projet_id>/', views.choix_projet, name='choix_projet'),
    
    path('generales/', views.generales, name='generales'),
    path('generales/ajouter_general/', views.ajouter_general, name='ajouter_general'),
    path('generales/modifier_general/', views.modifier_general, name='modifier_general'),
    path('generales/voir_general/', views.view_generale, name='view_generale' ),
    # path('projet/<int:projet_id>/choix_form/generales/ajouter_general/', views.ajouter_general, name='ajouter_general'),
    # path('projet/<int:projet_id>/choix_form/generales/modifier_general/<int:gen_id>/', views.modifier_general, name='modifier_general'),
    # path('projet/<int:projet_id>/choix_form/generales/voir_general/<int:gen_id>/', views.view_generale, name='view_generale'),

    path('projet/<int:projet_id>/choix_form/situation/', views.situation, name='situation'),
    path('projet/<int:projet_id>/choix_form/situation/ajouter_situation/', views.ajouter_situation, name='ajouter_situation'),
    path('projet/<int:projet_id>/choix_form/situation/modifier_situation/<int:situation_id>/', views.modifier_situation, name='modifier_situation'),
    path('projet/<int:projet_id>/choix_form/situation/voir_situation/<int:situation_id>/', views.view_situation, name='view_situation'),

    path('projet/<int:projet_id>/choix_form/planification/', views.activites, name='planification'),
    path('projet/<int:projet_id>/choix_form/planification/ajouter_planification/', views.ajouter_planification, name='ajouter_planification'),
    path('projet/<int:projet_id>/choix_form/planification/modifier_planification/<int:activite_id>/', views.modifier_planification, name='modifier_planification'),
    path('projet/<int:projet_id>/choix_form/planification/voir_planification/<int:activite_id>/', views.view_planification, name='view_planification'),

    path('projet/<int:projet_id>/choix_form/realisation/', views.realisation, name='realisation'),
    # path('projet/<int:projet_id>/choix_form/suivi/ajouter_activiter/', views.ajouter_suivi, name='ajouter_suivi'),
    path('projet/<int:projet_id>/choix_form/realisation/modifier_realisation/<int:activite_id>/', views.modifier_realisation, name="modifier_realisation"),
    # path('projet/<int:projet_id>/choix_form/realisation/modifier_activiter/<int:activite_id>/', views.modifier_realisation, name='modifier_realisation'),
    path('projet/<int:projet_id>/choix_form/realisation/voir_realisation/<int:activite_id>/', views.view_realisation, name='view_realisation'),

    path('projet/<int:projet_id>/choix_form/depense/', views.depense, name='depense'),
    path('projet/<int:projet_id>/choix_form/depense/ajouter_depense/', views.ajouter_depense, name='ajouter_depense'),
    path('projet/<int:projet_id>/choix_form/depense/modifier_depense/<int:depense_id>/', views.modifier_depense, name='modifier_depense'),
    path('projet/<int:projet_id>/choix_form/depense/voir_realisation/<int:depense_id>/', views.view_depense, name='view_depense'),
    
]
