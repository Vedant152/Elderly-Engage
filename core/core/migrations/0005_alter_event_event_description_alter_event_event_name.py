# Generated by Django 5.0 on 2023-12-22 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_alter_event_user_recommended"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="event_description",
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="event_name",
            field=models.CharField(max_length=60),
        ),
    ]
