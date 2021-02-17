# Generated by Django 3.1.6 on 2021-02-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('phone', models.CharField(help_text='Enter phone number without country code', max_length=10, verbose_name='Phone Number')),
                ('house_name', models.CharField(max_length=50, verbose_name='House Name')),
                ('locality', models.CharField(max_length=50)),
                ('pin_code', models.BigIntegerField()),
                ('ration_card', models.CharField(choices=[('APL', 'APL'), ('BPL', 'BPL')], max_length=10)),
                ('annual_income', models.IntegerField()),
                ('job', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
    ]
