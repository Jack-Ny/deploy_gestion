# Generated by Django 5.0.3 on 2024-04-18 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_remove_activites1_1_budget_prevu'),
    ]

    operations = [
        migrations.AddField(
            model_name='activites1_1',
            name='somme_part_etat_financier',
            field=models.IntegerField(default=0),
        ),
    ]