# Generated by Django 4.1.1 on 2022-11-04 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludoscienceapp', '0003_alter_proyect_time_restriction'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameelement',
            name='rate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
