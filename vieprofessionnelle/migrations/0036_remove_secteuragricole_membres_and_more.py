# Generated by Django 4.1.1 on 2022-11-17 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0035_membre_identifiant_alter_membre_nom_prenoms_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secteuragricole',
            name='membres',
        ),
        migrations.RemoveField(
            model_name='secteurfemmeactive',
            name='membres',
        ),
        migrations.RemoveField(
            model_name='secteurinformel',
            name='membres',
        ),
    ]
