# Generated by Django 5.0 on 2023-12-23 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_remove_registration_event_remove_registration_person_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female"), ("others", "Others")],
                max_length=10,
                null=True,
            ),
        ),
    ]
