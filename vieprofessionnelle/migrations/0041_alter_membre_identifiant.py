# Generated by Django 4.1.1 on 2022-11-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0040_alter_membre_nom_prenoms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='identifiant',
            field=models.CharField(blank=True, default=None, max_length=12, null=True, unique=True, verbose_name='Identifiant'),
        ),
    ]
