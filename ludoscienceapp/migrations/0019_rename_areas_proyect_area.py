# Generated by Django 4.1.1 on 2022-11-15 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ludoscienceapp', '0018_remove_proyect_areas_proyect_areas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyect',
            old_name='areas',
            new_name='area',
        ),
    ]