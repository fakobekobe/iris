# Generated by Django 4.1.1 on 2022-11-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secteur', models.CharField(max_length=250, unique=True)),
            ],
        ),
    ]
