# Generated by Django 5.0 on 2023-12-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="event_type",
            field=models.CharField(
                choices=[("health", "Health"), ("social", "Social")],
                max_length=10,
                null=True,
            ),
        ),
    ]
