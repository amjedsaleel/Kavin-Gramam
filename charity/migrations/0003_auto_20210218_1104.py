# Generated by Django 3.1.6 on 2021-02-18 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0002_auto_20210218_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='member',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='charity.member'),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='requirement',
            field=models.ManyToManyField(blank=True, to='charity.Category'),
        ),
    ]
