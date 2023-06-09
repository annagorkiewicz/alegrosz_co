# Generated by Django 4.1.7 on 2023-03-27 05:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.ImageField(upload_to="products")),
                ("stock_count", models.PositiveIntegerField()),
                ("slug", models.SlugField(blank=True)),
                (
                    "popularity",
                    models.PositiveIntegerField(
                        default=0, help_text="Incrementation " "when user checks details page."
                    ),
                ),
                ("rank", models.FloatField(default=0, help_text="Ranked by users.")),
                ("sales_count", models.PositiveIntegerField(default=0)),
                ("barcode", models.CharField(max_length=13, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
