import pytest

from django.urls import reverse

from pytest_django.asserts import assertTemplateUsed
from http import HTTPStatus

from .fixtures.item_fixture import ItemFactory


class TestView:

    @pytest.mark.django_db(transaction=True)
    def test_success_view(self, client):
        res = client.get(reverse('success'))

        assertTemplateUsed(res, 'success.html')
        assert res.status_code == HTTPStatus.OK

    @pytest.mark.django_db(transaction=True)
    def test_prductlanding_view(self, client):
        item = ItemFactory.create_batch(1)

        res = client.get(reverse('landing-page', kwargs={'pk': item[0].id}))

        assertTemplateUsed(res, 'landing.html')
        assert res.status_code == HTTPStatus.OK
