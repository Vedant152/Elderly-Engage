# Generated by Django 5.0 on 2023-12-23 18:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_alter_person_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
                max_length=10,
                null=True,
            ),
        ),
    ]