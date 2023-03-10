# Generated by Django 4.1.1 on 2022-11-21 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0041_alter_membre_identifiant'),
    ]

    operations = [
        migrations.AddField(
            model_name='etatsante',
            name='membre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vieprofessionnelle.membre'),
        ),
        migrations.AlterField(
            model_name='etatsante',
            name='dateenre',
            field=models.DateField(blank=True, default=None, null=True, verbose_name="Date d'enregistrement"),
        ),
    ]
