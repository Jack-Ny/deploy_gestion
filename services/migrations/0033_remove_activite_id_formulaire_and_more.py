# Generated by Django 5.0.3 on 2024-05-23 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0032_infosgenerale_total_pers_femme_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activite',
            name='id_formulaire',
        ),
        migrations.RemoveField(
            model_name='activite',
            name='id_orientation',
        ),
        migrations.RemoveField(
            model_name='activite',
            name='id_secteur',
        ),
        migrations.RemoveField(
            model_name='activiteplu',
            name='id_formulaire',
        ),
        migrations.RemoveField(
            model_name='activiteplu',
            name='id_orientation',
        ),
        migrations.RemoveField(
            model_name='activiteplu',
            name='id_secteur',
        ),
        migrations.AddField(
            model_name='soussecteur',
            name='secteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domaines', to='services.secteur'),
        ),
    ]
