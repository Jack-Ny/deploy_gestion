# Generated by Django 5.0.3 on 2024-05-23 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0033_remove_activite_id_formulaire_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='titreactivite',
            name='domaine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='titre_activite', to='services.soussecteur'),
        ),
    ]