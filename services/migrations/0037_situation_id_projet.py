# Generated by Django 5.0.3 on 2024-05-27 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0036_activite_id_secteur_activiteplu_id_secteur'),
    ]

    operations = [
        migrations.AddField(
            model_name='situation',
            name='id_projet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='situation', to='services.projet'),
        ),
    ]
