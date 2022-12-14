# Generated by Django 4.1.3 on 2022-12-08 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("espacecate", "0008_rename_child_enfant"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="hidden",
            field=models.BooleanField(default=False, verbose_name="Page cachée"),
        ),
        migrations.AddField(
            model_name="page",
            name="parent_page",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="espacecate.page",
                verbose_name="Page précédente",
            ),
        ),
    ]
