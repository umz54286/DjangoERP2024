# Generated by Django 4.2 on 2024-10-28 02:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("erp", "0012_alter_採購主檔_備註"),
    ]

    operations = [
        migrations.AlterField(
            model_name="採購明細",
            name="備註",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="銷售主檔",
            name="備註",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="銷售明細",
            name="備註",
            field=models.TextField(null=True),
        ),
    ]
