# Generated by Django 4.1.1 on 2022-11-01 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludoscienceapp', '0016_alter_proyect_description_alter_proyect_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameelement',
            name='goal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
