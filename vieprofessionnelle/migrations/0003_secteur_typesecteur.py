# Generated by Django 4.1.1 on 2022-11-01 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0002_secteur'),
    ]

    operations = [
        migrations.AddField(
            model_name='secteur',
            name='typesecteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vieprofessionnelle.typesecteur'),
        ),
    ]
