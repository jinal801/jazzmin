# Generated by Django 4.2.4 on 2023-08-02 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blood_request", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="RequestBlood",
        ),
    ]