# Generated by Django 4.1.1 on 2022-12-01 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alaapp', '0002_assignment_criteria_day_scoring_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='alaapp.user'),
        ),
    ]