# Generated by Django 4.1.1 on 2022-12-06 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0051_secteurfemmeactive_ville'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personneressource',
            name='chapeau',
        ),
        migrations.RemoveField(
            model_name='personneressource',
            name='membre',
        ),
    ]
