from django.core.validators import validate_slug
from django.db import models
from django.utils.text import slugify


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TimeStampModel):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products")
    stock_count = models.PositiveIntegerField()
    slug = models.SlugField(max_length=50, blank=True)
    popularity = models.PositiveIntegerField(default=0, help_text="Incrementation when user checks details page.")
    rank = models.FloatField(default=0, help_text="Ranked by users.")
    sales_count = models.PositiveIntegerField(default=0)
    barcode = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
