# Generated by Django 4.1.1 on 2022-11-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0032_secteurfemmeactive_marche_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secteurinformel',
            name='metier',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Métier'),
        ),
    ]
