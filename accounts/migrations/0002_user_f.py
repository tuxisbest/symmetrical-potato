# Generated by Django 4.1.3 on 2022-11-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="f",
            field=models.CharField(default="f", max_length=100),
        ),
    ]
