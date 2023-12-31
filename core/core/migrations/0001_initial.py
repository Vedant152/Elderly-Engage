# Generated by Django 5.0 on 2023-12-21 15:39

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                (
                    "age",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(60),
                            django.core.validators.MaxValueValidator(110),
                        ]
                    ),
                ),
                ("area", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=30)),
                (
                    "pincode",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(100000),
                            django.core.validators.MaxValueValidator(999999),
                        ]
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "phone",
                    models.CharField(blank=True, default="", max_length=13, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("event_name", models.CharField(max_length=30)),
                ("event_description", models.CharField(max_length=30, null=True)),
                ("event_date", models.DateField()),
                ("event_starttime", models.TimeField()),
                ("event_endtime", models.TimeField()),
                ("event_venue", models.CharField(max_length=30)),
                ("event_area", models.CharField(max_length=50)),
                ("event_city", models.CharField(max_length=30)),
                (
                    "event_pincode",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(100000),
                            django.core.validators.MaxValueValidator(999999),
                        ]
                    ),
                ),
                ("approved", models.BooleanField(default=False)),
                ("expired", models.BooleanField(default=False)),
                (
                    "user_recommended",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.person",
                    ),
                ),
            ],
        ),
    ]
