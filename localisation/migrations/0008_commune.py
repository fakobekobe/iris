# Generated by Django 4.1.1 on 2022-10-23 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localisation', '0007_rename_region_ville_departement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True)),
                ('libelle', models.CharField(max_length=250, unique=True, verbose_name='Commune')),
                ('ville', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='localisation.ville')),
            ],
        ),
    ]
