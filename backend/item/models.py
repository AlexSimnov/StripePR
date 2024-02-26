from django.db import models
from django.core.validators import MinValueValidator


class Item(models.Model):
    name = models.CharField(
        'имя',
        max_length=50
    )
    description = models.TextField(
        'описание',
        max_length=150
    )
    price = models.IntegerField(
        'цена',
        validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'вещь'
        verbose_name_plural = 'вещи'

    def __str__(self) -> str:
        return f'{self.name}'

    def get_price(self):
        return '{0:.2f}'.format(self.price / 100)
