import pytest
import factory

from item.models import Item


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    name = factory.Faker('name')
    description = factory.Faker('text')
    price = factory.Faker('random_int', min=1000, max=10000)
