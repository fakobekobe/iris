# Generated by Django 4.1.1 on 2022-11-09 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0007_typeparent_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='datenaissance',
            field=models.DateField(blank=True, null=True, verbose_name='Date de naissance'),
        ),
    ]
