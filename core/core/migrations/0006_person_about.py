# Generated by Django 5.0 on 2023-12-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_alter_event_event_description_alter_event_event_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="about",
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
