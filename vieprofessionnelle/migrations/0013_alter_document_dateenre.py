# Generated by Django 4.1.1 on 2022-11-11 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0012_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='dateenre',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 11, 13, 11, 45, 795175, tzinfo=datetime.timezone.utc), null=True, verbose_name="Date d'enregistrement"),
        ),
    ]
