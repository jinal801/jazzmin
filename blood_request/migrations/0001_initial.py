# Generated by Django 4.2.4 on 2023-08-02 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("donor", "0003_donor"),
    ]

    operations = [
        migrations.CreateModel(
            name="RequestBlood",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("state", models.CharField(blank=True, max_length=200)),
                ("city", models.CharField(blank=True, max_length=300)),
                ("address", models.CharField(blank=True, max_length=500)),
                ("date", models.CharField(blank=True, max_length=100)),
                (
                    "blood_group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="donor.bloodgroup",
                    ),
                ),
            ],
        ),
    ]