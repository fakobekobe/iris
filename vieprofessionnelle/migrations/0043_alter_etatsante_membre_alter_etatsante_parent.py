# Generated by Django 4.1.1 on 2022-11-21 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0042_etatsante_membre_alter_etatsante_dateenre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etatsante',
            name='membre',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vieprofessionnelle.membre'),
        ),
        migrations.AlterField(
            model_name='etatsante',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vieprofessionnelle.parent'),
        ),
    ]