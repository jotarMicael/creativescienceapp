# Generated by Django 4.1.1 on 2022-11-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludoscienceapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameelement',
            name='public',
            field=models.IntegerField(default=1),
        ),
    ]
