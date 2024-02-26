import pytest

from http import HTTPStatus

from .fixtures.item_fixture import ItemFactory


class TestView:

    item_url = '/item/'
    success_url = '/success/'

    @pytest.mark.django_db(transaction=True)
    def test_items_url(self, client):
        items = ItemFactory.create_batch(10)

        for i in items:
            res = client.get(self.item_url+f'{i.id}/')

            assert res.status_code == HTTPStatus.OK

    @pytest.mark.django_db(transaction=True)
    def test_success_url(self, client):

        res = client.get('/success/')

        assert res.status_code == HTTPStatus.OK
