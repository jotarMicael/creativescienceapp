# Generated by Django 4.1.1 on 2022-11-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludoscienceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyect',
            name='time_restriction',
            field=models.ManyToManyField(related_name='time_retrictions', to='ludoscienceapp.timerestriction'),
        ),
    ]
