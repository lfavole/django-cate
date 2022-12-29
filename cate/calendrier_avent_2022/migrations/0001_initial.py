# Generated by Django 4.1.3 on 2022-12-23 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Day",
            fields=[
                (
                    "jour",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="Jour"
                    ),
                ),
                ("enfant", models.CharField(max_length=100, verbose_name="Enfant")),
                (
                    "photo",
                    filer.fields.image.FilerImageField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.FILER_IMAGE_MODEL,
                    ),
                ),
            ],
        ),
    ]
