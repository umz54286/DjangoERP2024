# Generated by Django 4.2 on 2024-10-28 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("erp", "0006_remove_銷售明細_id_alter_銷售明細_產品_alter_銷售明細_銷售主檔"),
    ]

    operations = [
        migrations.AlterField(
            model_name="銷售主檔",
            name="客戶",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="erp.客戶"
            ),
        ),
    ]
