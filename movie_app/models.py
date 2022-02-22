from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


""" Создание модели(базы данных) """


class Movie(models.Model):
    """ Константы для формы choices """
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (RUB, 'Rubles'),
        (USD, 'Dollars')
    ]

    """ Поля в базе данных """
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(1)])
    slug = models.SlugField(default='', null=False, db_index=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='R')

    """Перегрузка метода save, занесение slug в БД"""

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Movie, self).save(*args, **kwargs)

    """Получение URL'a по name (slug)"""

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    """Перегрузка метода __str__, для отображение поля"""

    def __str__(self):
        return f'{self.name} - {self.rating} {self.year}'
