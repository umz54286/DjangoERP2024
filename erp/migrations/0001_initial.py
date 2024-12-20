# Generated by Django 4.2 on 2024-10-24 02:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="供應商",
            fields=[
                ("序號", models.AutoField(primary_key=True, serialize=False)),
                ("供應商編號", models.CharField(max_length=20)),
                ("供應商名稱", models.CharField(max_length=50)),
                ("聯絡人", models.CharField(max_length=30)),
                ("電話", models.CharField(max_length=20)),
                ("地址", models.CharField(max_length=100)),
                ("統一編號", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="客戶",
            fields=[
                ("序號", models.AutoField(primary_key=True, serialize=False)),
                ("客戶編號", models.CharField(max_length=20)),
                ("客戶名稱", models.CharField(max_length=50)),
                ("聯絡人", models.CharField(max_length=30)),
                ("電話", models.CharField(max_length=20)),
                ("地址", models.CharField(max_length=100)),
                ("統一編號", models.CharField(max_length=10)),
            ],
        ),
    ]
