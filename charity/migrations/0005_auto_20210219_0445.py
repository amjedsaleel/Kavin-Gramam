# Generated by Django 3.1.6 on 2021-02-19 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0004_auto_20210218_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='requirement',
            field=models.ManyToManyField(blank=True, to='charity.Category'),
        ),
    ]
