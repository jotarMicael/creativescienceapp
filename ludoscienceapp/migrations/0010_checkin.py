# Generated by Django 4.1.1 on 2022-11-04 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ludoscienceapp', '0009_alter_user_proyects'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=500)),
                ('longitude', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField()),
                ('proyect', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ludoscienceapp.proyect')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ludoscienceapp.user')),
            ],
            options={
                'verbose_name': 'CheckIn',
                'verbose_name_plural': 'CheckIns',
                'db_table': 'check_in',
            },
        ),
    ]
