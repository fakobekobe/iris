# Generated by Django 4.1.1 on 2022-10-19 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localisation', '0004_departement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departement',
            old_name='district',
            new_name='region',
        ),
    ]
