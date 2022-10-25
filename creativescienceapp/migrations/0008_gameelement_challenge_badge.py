# Generated by Django 4.1.1 on 2022-10-25 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("creativescienceapp", "0007_proyect_avaliable"),
    ]

    operations = [
        migrations.CreateModel(
            name="GameElement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("area", models.CharField(max_length=150)),
                ("time_restriction", models.DateTimeField()),
                ("goal", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Challenge",
            fields=[
                (
                    "gameelement_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="creativescienceapp.gameelement",
                    ),
                ),
            ],
            bases=("creativescienceapp.gameelement",),
        ),
        migrations.CreateModel(
            name="Badge",
            fields=[
                (
                    "gameelement_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="creativescienceapp.gameelement",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="creativescience/creativescienceapp/static/game_elements_image/ge.jpg",
                        upload_to="creativescience/creativescienceapp/static/game_elements_image/",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="creativescienceapp.badge",
                    ),
                ),
            ],
            bases=("creativescienceapp.gameelement",),
        ),
    ]
