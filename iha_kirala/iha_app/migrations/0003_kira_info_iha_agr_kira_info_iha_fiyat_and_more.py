# Generated by Django 4.1.1 on 2022-11-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iha_app", "0002_kira_info_delete_register_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="kira_info",
            name="iha_agr",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="kira_info",
            name="iha_fiyat",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="kira_info", name="iha_kat", field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="kira_info",
            name="iha_marka",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="kira_info",
            name="iha_model",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="kira_info",
            name="iha_kac_gün",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="kira_info",
            name="iha_kullanıcı",
            field=models.TextField(default=""),
        ),
    ]