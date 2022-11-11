# Generated by Django 4.1.1 on 2022-11-11 17:40

import datetime
from django.db import migrations, models
import vieprofessionnelle.models


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0020_alter_document_dateenre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='dateenre',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 11, 17, 40, 51, 563699, tzinfo=datetime.timezone.utc), null=True, verbose_name="Date d'enregistrement"),
        ),
        migrations.AlterField(
            model_name='document',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=vieprofessionnelle.models.nomfichier),
        ),
    ]
