# Generated by Django 4.1.1 on 2022-11-09 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0005_rename_membre_secteuragricole_membres_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='secteurfemmeactive',
            name='membres',
            field=models.ManyToManyField(to='vieprofessionnelle.membre'),
        ),
        migrations.RemoveField(
            model_name='secteurfemmeactive',
            name='personne_ressource',
        ),
        migrations.AddField(
            model_name='secteurfemmeactive',
            name='personne_ressource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personne_membre_set', to='vieprofessionnelle.membre'),
        ),
    ]
