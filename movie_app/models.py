from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


class Movie(models.Model):
    EUR = "EUR"
    USD = "USD"
    RUB = "RUB"
    CURRENCY_CHOICES = [(EUR, "Euro"), (RUB, "Rubles"), (USD, "Dollars")]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(1)])
    slug = models.SlugField(default="", null=False, db_index=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="R")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("movie-detail", args=[self.slug])

    def __str__(self):
        return f"{self.name} - {self.rating} {self.year}"
