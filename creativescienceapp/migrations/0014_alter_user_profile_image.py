# Generated by Django 4.1.1 on 2022-10-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("creativescienceapp", "0013_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_image",
            field=models.ImageField(
                blank=True,
                default="creativescienceapp/static/profile_image/cover.jpg",
                null=True,
                upload_to="creativescienceapp/static/profile_image/user.png",
            ),
        ),
    ]
