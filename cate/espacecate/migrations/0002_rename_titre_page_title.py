# Generated by Django 4.1.3 on 2022-12-07 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("espacecate", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="page",
            old_name="titre",
            new_name="title",
        ),
    ]
