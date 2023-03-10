# Generated by Django 4.1.1 on 2022-12-31 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vieprofessionnelle', '0055_remove_secteuragricole_gps_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membresecteuragricole',
            name='gps_latitude',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='GPS Latitude'),
        ),
        migrations.AlterField(
            model_name='membresecteuragricole',
            name='gps_longitude',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='GPS Longitude'),
        ),
        migrations.AlterField(
            model_name='membresecteurfemmeactive',
            name='gps_latitude',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='GPS Latitude'),
        ),
        migrations.AlterField(
            model_name='membresecteurfemmeactive',
            name='gps_longitude',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='GPS Longitude'),
        ),
        migrations.AlterField(
            model_name='membresecteurinformel',
            name='gps_latitude',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='GPS Latitude'),
        ),
        migrations.AlterField(
            model_name='membresecteurinformel',
            name='gps_longitude',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='GPS Longitude'),
        ),
    ]
