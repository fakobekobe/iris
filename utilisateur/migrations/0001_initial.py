# Generated by Django 4.1.1 on 2022-12-05 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parametre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monnaie', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('id_chapeau', models.CharField(blank=True, default='', max_length=10, null=True)),
            ],
        ),
    ]
