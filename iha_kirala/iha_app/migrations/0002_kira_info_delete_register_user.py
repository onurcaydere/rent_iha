# Generated by Django 4.1.1 on 2022-11-10 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iha_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="kira_info",
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
                ("iha_kullanıcı", models.TextField()),
                ("iha_kac_gün", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(name="register_user",),
    ]