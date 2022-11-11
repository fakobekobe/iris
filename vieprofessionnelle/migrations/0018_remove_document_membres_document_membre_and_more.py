# Generated by Django 4.1.1 on 2022-11-11 15:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0017_alter_document_dateenre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='membres',
        ),
        migrations.AddField(
            model_name='document',
            name='membre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vieprofessionnelle.membre'),
        ),
        migrations.AlterField(
            model_name='document',
            name='dateenre',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 11, 15, 8, 12, 638322, tzinfo=datetime.timezone.utc), null=True, verbose_name="Date d'enregistrement"),
        ),
    ]
