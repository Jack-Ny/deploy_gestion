# Generated by Django 5.0.3 on 2024-07-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0046_remove_infosspecific_resultats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosspecific',
            name='nom',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='infosspecific',
            name='objectifs_principals',
            field=models.CharField(max_length=200),
        ),
    ]