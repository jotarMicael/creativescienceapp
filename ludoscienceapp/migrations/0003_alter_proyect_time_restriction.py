# Generated by Django 4.1.1 on 2022-11-03 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludoscienceapp', '0002_alter_proyect_time_restriction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyect',
            name='time_restriction',
            field=models.ManyToManyField(to='ludoscienceapp.timerestriction'),
        ),
    ]
