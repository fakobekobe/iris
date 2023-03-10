# Generated by Django 4.1.1 on 2022-12-23 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localisation', '0010_marche'),
        ('vieprofessionnelle', '0053_personneressource_chapeau_personneressource_membre'),
    ]

    operations = [
        migrations.AddField(
            model_name='secteuragricole',
            name='ville',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='localisation.ville'),
        ),
        migrations.AddField(
            model_name='secteurinformel',
            name='ville',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='localisation.ville'),
        ),
    ]
