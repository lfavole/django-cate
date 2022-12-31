# Generated by Django 4.1.3 on 2022-12-31 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("espacecate", "0018_remove_espacecateuservisit_hash"),
    ]

    operations = [
        migrations.AddField(
            model_name="espacecateuservisit",
            name="hash",
            field=models.CharField(
                default="",
                help_text="MD5 hash generated from request properties",
                max_length=32,
            ),
            preserve_default=False,
        ),
    ]
