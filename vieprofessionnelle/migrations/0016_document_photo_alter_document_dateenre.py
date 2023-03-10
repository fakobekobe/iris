# Generated by Django 4.1.1 on 2022-11-11 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0015_alter_document_dateenre'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='document',
            name='dateenre',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 11, 13, 47, 26, 86124, tzinfo=datetime.timezone.utc), null=True, verbose_name="Date d'enregistrement"),
        ),
    ]
