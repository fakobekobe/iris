# Generated by Django 4.1.1 on 2022-12-03 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0046_typepersonneressource_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MontantFinancement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.IntegerField(unique=True, verbose_name='Montant')),
            ],
        ),
        migrations.CreateModel(
            name='QuantiteGroupement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField(unique=True, verbose_name='Quantité')),
            ],
        ),
        migrations.CreateModel(
            name='TypeResponsabilite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='membresecteurfemmeactive',
            name='personneressource',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vieprofessionnelle.personneressource'),
        ),
        migrations.AddField(
            model_name='secteurfemmeactive',
            name='identifiant',
            field=models.CharField(blank=True, default=None, max_length=19, null=True, unique=True, verbose_name='Identifiant'),
        ),
        migrations.AddField(
            model_name='membresecteurfemmeactive',
            name='montantfinancement',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vieprofessionnelle.montantfinancement'),
        ),
        migrations.AddField(
            model_name='membresecteurfemmeactive',
            name='typeresponsabilite',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vieprofessionnelle.typeresponsabilite'),
        ),
        migrations.AddField(
            model_name='secteurfemmeactive',
            name='quantitegroupement',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vieprofessionnelle.quantitegroupement'),
        ),
    ]
