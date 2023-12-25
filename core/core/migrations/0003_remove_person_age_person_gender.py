# Generated by Django 5.0 on 2023-12-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_event_event_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="age",
        ),
        migrations.AddField(
            model_name="person",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female")],
                max_length=10,
                null=True,
            ),
        ),
    ]