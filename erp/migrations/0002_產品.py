# Generated by Django 4.2 on 2024-10-28 01:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("erp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="產品",
            fields=[
                ("供應商名稱", models.CharField(max_length=50)),
                ("聯絡人", models.CharField(max_length=30)),
                ("電話", models.CharField(max_length=20)),
                ("地址", models.CharField(max_length=100)),
                ("統一編號", models.CharField(max_length=10)),
                ("序號", models.AutoField(primary_key=True, serialize=False)),
                ("產品編號", models.CharField(max_length=20)),
                ("產品名稱", models.CharField(max_length=50)),
                ("產品描述", models.TextField()),
                ("類別", models.CharField(max_length=20)),
                ("單位", models.CharField(max_length=10)),
                ("進貨成本", models.DecimalField(decimal_places=0, max_digits=2)),
                ("售價", models.DecimalField(decimal_places=0, max_digits=2)),
                ("庫存量", models.IntegerField()),
                ("安全庫存量", models.IntegerField()),
                ("供應商編號", models.IntegerField()),
            ],
        ),
    ]
