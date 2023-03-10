# Generated by Django 4.1.1 on 2022-12-03 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localisation', '0010_marche'),
        ('vieprofessionnelle', '0047_montantfinancement_quantitegroupement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='membresecteuragricole',
            name='chapeau',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vieprofessionnelle.chapeau'),
        ),
        migrations.AddField(
            model_name='membresecteurfemmeactive',
            name='chapeau',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vieprofessionnelle.chapeau'),
        ),
        migrations.AddField(
            model_name='membresecteurinformel',
            name='chapeau',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vieprofessionnelle.chapeau'),
        ),
        migrations.AddField(
            model_name='secteurfemmeactive',
            name='quartier',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='localisation.quartier'),
        ),
    ]
