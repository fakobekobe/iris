# Generated by Django 4.1.1 on 2022-12-31 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0005_parametre_id_accident_parametre_id_deces'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametre',
            name='id_conseillere1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parametre',
            name='id_conseillere2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parametre',
            name='id_responsable',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parametre',
            name='id_tresoriere',
            field=models.IntegerField(default=0),
        ),
    ]