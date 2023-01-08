# Generated by Django 4.1.3 on 2023-01-01 11:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ("filer", "0015_alter_file_owner_alter_file_polymorphic_ctype_and_more"),
        ("espacecate", "0019_espacecateuservisit_hash"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="EspacecateUserVisit",
            new_name="UserVisit",
        ),
        migrations.AlterModelOptions(
            name="article",
            options={"verbose_name": "Article"},
        ),
        migrations.AlterModelOptions(
            name="document",
            options={"verbose_name": "Document"},
        ),
        migrations.AlterModelOptions(
            name="page",
            options={"ordering": ["order"], "verbose_name": "Page"},
        ),
        migrations.AlterField(
            model_name="child",
            name="annee_pardon",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1970),
                    django.core.validators.MaxValueValidator(2023),
                ],
                verbose_name="Année du Sacrement du Pardon",
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="file",
            field=filer.fields.file.FilerFileField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="filer.file",
                verbose_name="Document",
            ),
        ),
    ]