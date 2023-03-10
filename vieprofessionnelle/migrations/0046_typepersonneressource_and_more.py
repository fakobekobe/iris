# Generated by Django 4.1.1 on 2022-12-03 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0045_remove_secteuragricole_chapeau_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypePersonneRessource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='secteurfemmeactive',
            name='personne_ressource',
        ),
        migrations.CreateModel(
            name='PersonneRessource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapeau', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vieprofessionnelle.chapeau')),
                ('membre', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vieprofessionnelle.membre')),
                ('typepersonneressource', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vieprofessionnelle.typepersonneressource')),
            ],
        ),
    ]
